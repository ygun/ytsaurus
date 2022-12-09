#include <yt/yt/core/test_framework/framework.h>

#include <yt/yt/core/ytree/convert.h>

#include <yt/yt/server/lib/io/io_engine.h>

#include <util/system/fs.h>
#include <util/system/tempfile.h>

#include <yt/yt/library/profiling/producer.h>
#include <yt/yt/library/containers/config.h>
#include <yt/yt/library/containers/porto_executor.h>
#include <yt/yt/library/containers/porto_resource_tracker.h>
#include <yt/yt/library/containers/instance.h>

#include <util/system/platform.h>
#include <util/system/env.h>

namespace NYT::NContainers {
namespace {

using namespace NIO;
using namespace NConcurrency;

////////////////////////////////////////////////////////////////////////////////

static constexpr auto TestUpdatePeriod = TDuration::MilliSeconds(10);

class TPortoTrackerTest
    : public ::testing::Test
{
public:
    IPortoExecutorPtr Executor;

    void SetUp() override
    {
        if (GetEnv("SKIP_PORTO_TESTS") != "") {
            GTEST_SKIP();
        }
        Executor = CreatePortoExecutor(New<TPortoExecutorConfig>(), "default");
    }
};

TString GetUniqueName()
{
    return "yt_porto_ut_" + ToString(TGuid::Create());
}

TPortoResourceTrackerPtr CreateSumPortoTracker(IPortoExecutorPtr Executor, const TString& name)
{
    return New<TPortoResourceTracker>(
        GetPortoInstance(Executor, name),
        TestUpdatePeriod,
        false
    );
}

TPortoResourceTrackerPtr CreateDeltaPortoTracker(IPortoExecutorPtr Executor, const TString& name)
{
    return New<TPortoResourceTracker>(
        GetPortoInstance(Executor, name),
        TestUpdatePeriod,
        true
    );
}

TEST_F(TPortoTrackerTest, ValidateSummaryPortoTracker)
{
    auto name = GetUniqueName();

    WaitFor(Executor->CreateContainer(
        TRunnableContainerSpec {
            .Name = name,
            .Command = "sleep .1",
        }, true))
        .ThrowOnError();

    auto tracker = CreateSumPortoTracker(Executor, name);

    auto firstStatistics = tracker->GetTotalStatistics();

    WaitFor(Executor->StopContainer(name))
        .ThrowOnError();
    WaitFor(Executor->SetContainerProperty(
        name,
        "command",
        "find /"))
        .ThrowOnError();
    WaitFor(Executor->StartContainer(name))
        .ThrowOnError();
    Sleep(TDuration::MilliSeconds(500));

    auto secondStatistics = tracker->GetTotalStatistics();

    WaitFor(Executor->DestroyContainer(name))
        .ThrowOnError();
}

TEST_F(TPortoTrackerTest, ValidateDeltaPortoTracker)
{
    auto name = GetUniqueName();

    auto spec = TRunnableContainerSpec {
        .Name = name,
        .Command = "sleep .1",
    };

    WaitFor(Executor->CreateContainer(spec, true))
        .ThrowOnError();

    auto tracker = CreateDeltaPortoTracker(Executor, name);
    auto firstStatistics = tracker->GetTotalStatistics();

    WaitFor(Executor->StopContainer(name))
        .ThrowOnError();
    WaitFor(Executor->SetContainerProperty(
        name,
        "command",
        "find /"))
        .ThrowOnError();
    WaitFor(Executor->StartContainer(name))
        .ThrowOnError();

    Sleep(TDuration::MilliSeconds(500));

    auto secondStatistics = tracker->GetTotalStatistics();
    auto profiler = New<TPortoResourceProfiler>(tracker);
    auto buffer = New<TSensorBuffer>();
    profiler->CollectSensors(buffer.Get());
    auto gauges = buffer->GetGauges();

    WaitFor(Executor->DestroyContainer(name))
        .ThrowOnError();
}

////////////////////////////////////////////////////////////////////////////////

} // namespace
} // namespace NYT::NContainers