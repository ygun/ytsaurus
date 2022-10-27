# Stubs for pyspark.context (Python 3.5)
#

from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, TypeVar

from py4j.java_gateway import JavaGateway, JavaObject  # type: ignore

from pyspark.accumulators import Accumulator, AccumulatorParam
from pyspark.broadcast import Broadcast
from pyspark.conf import SparkConf
from pyspark.profiler import Profiler
from pyspark.resourceinformation import ResourceInformation
from pyspark.rdd import RDD
from pyspark.serializers import Serializer
from pyspark.status import StatusTracker

T = TypeVar("T")
U = TypeVar("U")

class SparkContext:
    PACKAGE_EXTENSIONS: Iterable[str]
    def __init__(
        self,
        master: Optional[str] = ...,
        appName: Optional[str] = ...,
        sparkHome: Optional[str] = ...,
        pyFiles: Optional[List[str]] = ...,
        environment: Optional[Dict[str, str]] = ...,
        batchSize: int = ...,
        serializer: Serializer = ...,
        conf: Optional[SparkConf] = ...,
        gateway: Optional[JavaGateway] = ...,
        jsc: Optional[JavaObject] = ...,
        profiler_cls: type = ...,
    ) -> None: ...
    def __getnewargs__(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, trace): ...
    @classmethod
    def getOrCreate(cls, conf: Optional[SparkConf] = ...) -> SparkContext: ...
    def setLogLevel(self, logLevel: str) -> None: ...
    @classmethod
    def setSystemProperty(cls, key: str, value: str) -> None: ...
    @property
    def version(self) -> str: ...
    @property
    def applicationId(self) -> str: ...
    @property
    def uiWebUrl(self) -> str: ...
    @property
    def startTime(self) -> int: ...
    @property
    def defaultParallelism(self) -> int: ...
    @property
    def defaultMinPartitions(self) -> int: ...
    def stop(self) -> None: ...
    def emptyRDD(self) -> RDD[None]: ...
    def range(
        self,
        start: int,
        end: Optional[int] = ...,
        step: int = ...,
        numSlices: Optional[int] = ...,
    ) -> RDD[int]: ...
    def parallelize(self, c: Iterable[T], numSlices: Optional[int] = ...) -> RDD[T]: ...
    def pickleFile(self, name: str, minPartitions: Optional[int] = ...) -> RDD[Any]: ...
    def textFile(
        self, name: str, minPartitions: Optional[int] = ..., use_unicode: bool = ...
    ) -> RDD[str]: ...
    def wholeTextFiles(
        self, path: str, minPartitions: Optional[int] = ..., use_unicode: bool = ...
    ) -> RDD[Tuple[str, str]]: ...
    def binaryFiles(
        self, path: str, minPartitions: Optional[int] = ...
    ) -> RDD[Tuple[str, bytes]]: ...
    def binaryRecords(self, path: str, recordLength: int) -> RDD[bytes]: ...
    def sequenceFile(
        self,
        path: str,
        keyClass: Optional[str] = ...,
        valueClass: Optional[str] = ...,
        keyConverter: Optional[str] = ...,
        valueConverter: Optional[str] = ...,
        minSplits: Optional[int] = ...,
        batchSize: int = ...,
    ) -> RDD[Tuple[T, U]]: ...
    def newAPIHadoopFile(
        self,
        path: str,
        inputFormatClass: str,
        keyClass: str,
        valueClass: str,
        keyConverter: Optional[str] = ...,
        valueConverter: Optional[str] = ...,
        conf: Optional[Dict[str, str]] = ...,
        batchSize: int = ...,
    ) -> RDD[Tuple[T, U]]: ...
    def newAPIHadoopRDD(
        self,
        inputFormatClass: str,
        keyClass: str,
        valueClass: str,
        keyConverter: Optional[str] = ...,
        valueConverter: Optional[str] = ...,
        conf: Optional[Dict[str, str]] = ...,
        batchSize: int = ...,
    ) -> RDD[Tuple[T, U]]: ...
    def hadoopFile(
        self,
        path: str,
        inputFormatClass: str,
        keyClass: str,
        valueClass: str,
        keyConverter: Optional[str] = ...,
        valueConverter: Optional[str] = ...,
        conf: Optional[Dict[str, str]] = ...,
        batchSize: int = ...,
    ) -> RDD[Tuple[T, U]]: ...
    def hadoopRDD(
        self,
        inputFormatClass: str,
        keyClass: str,
        valueClass: str,
        keyConverter: Optional[str] = ...,
        valueConverter: Optional[str] = ...,
        conf: Optional[Dict[str, str]] = ...,
        batchSize: int = ...,
    ) -> RDD[Tuple[T, U]]: ...
    def union(self, rdds: Iterable[RDD[T]]) -> RDD[T]: ...
    def broadcast(self, value: T) -> Broadcast[T]: ...
    def accumulator(
        self, value: T, accum_param: Optional[AccumulatorParam[T]] = ...
    ) -> Accumulator[T]: ...
    def addFile(self, path: str, recursive: bool = ...) -> None: ...
    def addPyFile(self, path: str) -> None: ...
    def setCheckpointDir(self, dirName: str) -> None: ...
    def setJobGroup(
        self, groupId: str, description: str, interruptOnCancel: bool = ...
    ) -> None: ...
    def setLocalProperty(self, key: str, value: str) -> None: ...
    def getLocalProperty(self, key: str) -> Optional[str]: ...
    def sparkUser(self) -> str: ...
    def setJobDescription(self, value: str) -> None: ...
    def cancelJobGroup(self, groupId: str) -> None: ...
    def cancelAllJobs(self) -> None: ...
    def statusTracker(self) -> StatusTracker: ...
    def runJob(
        self,
        rdd: RDD[T],
        partitionFunc: Callable[[Iterable[T]], Iterable[U]],
        partitions: Optional[List[int]] = ...,
        allowLocal: bool = ...,
    ) -> List[U]: ...
    def show_profiles(self) -> None: ...
    def dump_profiles(self, path: str) -> None: ...
    def getConf(self) -> SparkConf: ...
    @property
    def resources(self) -> Dict[str, ResourceInformation]: ...