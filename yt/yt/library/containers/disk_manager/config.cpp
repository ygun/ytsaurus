#include "config.h"

namespace NYT::NContainers {

////////////////////////////////////////////////////////////////////////////////

void TDiskManagerProxyConfig::Register(TRegistrar registrar)
{
    registrar.Parameter("health_check_timeout", &TThis::RequestTimeout)
        .Default(TDuration::Seconds(10));
}

////////////////////////////////////////////////////////////////////////////////

void TDiskManagerProxyDynamicConfig::Register(TRegistrar registrar)
{
    registrar.Parameter("health_check_timeout", &TThis::RequestTimeout)
        .Default();
}

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NContainers