# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import milvus_pb2 as milvus__pb2
from . import status_pb2 as status__pb2


class MilvusServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/CreateCollection',
        request_serializer=milvus__pb2.CollectionSchema.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.HasCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/HasCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.BoolReply.FromString,
        )
    self.DescribeCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/DescribeCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.CollectionSchema.FromString,
        )
    self.CountCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/CountCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.CollectionRowCount.FromString,
        )
    self.ShowCollections = channel.unary_unary(
        '/milvus.grpc.MilvusService/ShowCollections',
        request_serializer=milvus__pb2.Command.SerializeToString,
        response_deserializer=milvus__pb2.CollectionNameList.FromString,
        )
    self.ShowCollectionInfo = channel.unary_unary(
        '/milvus.grpc.MilvusService/ShowCollectionInfo',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.CollectionInfo.FromString,
        )
    self.DropCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/DropCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.CreateIndex = channel.unary_unary(
        '/milvus.grpc.MilvusService/CreateIndex',
        request_serializer=milvus__pb2.IndexParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.DescribeIndex = channel.unary_unary(
        '/milvus.grpc.MilvusService/DescribeIndex',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.IndexParam.FromString,
        )
    self.DropIndex = channel.unary_unary(
        '/milvus.grpc.MilvusService/DropIndex',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.CreatePartition = channel.unary_unary(
        '/milvus.grpc.MilvusService/CreatePartition',
        request_serializer=milvus__pb2.PartitionParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.HasPartition = channel.unary_unary(
        '/milvus.grpc.MilvusService/HasPartition',
        request_serializer=milvus__pb2.PartitionParam.SerializeToString,
        response_deserializer=milvus__pb2.BoolReply.FromString,
        )
    self.ShowPartitions = channel.unary_unary(
        '/milvus.grpc.MilvusService/ShowPartitions',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.PartitionList.FromString,
        )
    self.DropPartition = channel.unary_unary(
        '/milvus.grpc.MilvusService/DropPartition',
        request_serializer=milvus__pb2.PartitionParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.Insert = channel.unary_unary(
        '/milvus.grpc.MilvusService/Insert',
        request_serializer=milvus__pb2.InsertParam.SerializeToString,
        response_deserializer=milvus__pb2.VectorIds.FromString,
        )
    self.GetVectorsByID = channel.unary_unary(
        '/milvus.grpc.MilvusService/GetVectorsByID',
        request_serializer=milvus__pb2.VectorsIdentity.SerializeToString,
        response_deserializer=milvus__pb2.VectorsData.FromString,
        )
    self.GetVectorIDs = channel.unary_unary(
        '/milvus.grpc.MilvusService/GetVectorIDs',
        request_serializer=milvus__pb2.GetVectorIDsParam.SerializeToString,
        response_deserializer=milvus__pb2.VectorIds.FromString,
        )
    self.Search = channel.unary_unary(
        '/milvus.grpc.MilvusService/Search',
        request_serializer=milvus__pb2.SearchParam.SerializeToString,
        response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
    self.SearchByID = channel.unary_unary(
        '/milvus.grpc.MilvusService/SearchByID',
        request_serializer=milvus__pb2.SearchByIDParam.SerializeToString,
        response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
    self.SearchInFiles = channel.unary_unary(
        '/milvus.grpc.MilvusService/SearchInFiles',
        request_serializer=milvus__pb2.SearchInFilesParam.SerializeToString,
        response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
    self.Cmd = channel.unary_unary(
        '/milvus.grpc.MilvusService/Cmd',
        request_serializer=milvus__pb2.Command.SerializeToString,
        response_deserializer=milvus__pb2.StringReply.FromString,
        )
    self.DeleteByID = channel.unary_unary(
        '/milvus.grpc.MilvusService/DeleteByID',
        request_serializer=milvus__pb2.DeleteByIDParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.PreloadCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/PreloadCollection',
        request_serializer=milvus__pb2.PreloadCollectionParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.ReleaseCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/ReleaseCollection',
        request_serializer=milvus__pb2.PreloadCollectionParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.ReloadSegments = channel.unary_unary(
        '/milvus.grpc.MilvusService/ReloadSegments',
        request_serializer=milvus__pb2.ReLoadSegmentsParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.Flush = channel.unary_unary(
        '/milvus.grpc.MilvusService/Flush',
        request_serializer=milvus__pb2.FlushParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.Compact = channel.unary_unary(
        '/milvus.grpc.MilvusService/Compact',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.CreateHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/CreateHybridCollection',
        request_serializer=milvus__pb2.Mapping.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.HasHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/HasHybridCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.BoolReply.FromString,
        )
    self.DropHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/DropHybridCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.DescribeHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/DescribeHybridCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.Mapping.FromString,
        )
    self.CountHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/CountHybridCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.CollectionRowCount.FromString,
        )
    self.ShowHybridCollections = channel.unary_unary(
        '/milvus.grpc.MilvusService/ShowHybridCollections',
        request_serializer=milvus__pb2.Command.SerializeToString,
        response_deserializer=milvus__pb2.MappingList.FromString,
        )
    self.ShowHybridCollectionInfo = channel.unary_unary(
        '/milvus.grpc.MilvusService/ShowHybridCollectionInfo',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=milvus__pb2.CollectionInfo.FromString,
        )
    self.PreloadHybridCollection = channel.unary_unary(
        '/milvus.grpc.MilvusService/PreloadHybridCollection',
        request_serializer=milvus__pb2.CollectionName.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )
    self.InsertEntity = channel.unary_unary(
        '/milvus.grpc.MilvusService/InsertEntity',
        request_serializer=milvus__pb2.HInsertParam.SerializeToString,
        response_deserializer=milvus__pb2.HEntityIDs.FromString,
        )
    self.HybridSearch = channel.unary_unary(
        '/milvus.grpc.MilvusService/HybridSearch',
        request_serializer=milvus__pb2.HSearchParam.SerializeToString,
        response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
    self.HybridSearchInSegments = channel.unary_unary(
        '/milvus.grpc.MilvusService/HybridSearchInSegments',
        request_serializer=milvus__pb2.HSearchInSegmentsParam.SerializeToString,
        response_deserializer=milvus__pb2.TopKQueryResult.FromString,
        )
    self.GetEntityByID = channel.unary_unary(
        '/milvus.grpc.MilvusService/GetEntityByID',
        request_serializer=milvus__pb2.HEntityIdentity.SerializeToString,
        response_deserializer=milvus__pb2.HEntity.FromString,
        )
    self.GetEntityIDs = channel.unary_unary(
        '/milvus.grpc.MilvusService/GetEntityIDs',
        request_serializer=milvus__pb2.HGetEntityIDsParam.SerializeToString,
        response_deserializer=milvus__pb2.HEntityIDs.FromString,
        )
    self.DeleteEntitiesByID = channel.unary_unary(
        '/milvus.grpc.MilvusService/DeleteEntitiesByID',
        request_serializer=milvus__pb2.HDeleteByIDParam.SerializeToString,
        response_deserializer=status__pb2.Status.FromString,
        )


class MilvusServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateCollection(self, request, context):
    """*
    @brief This method is used to create collection

    @param CollectionSchema, use to provide collection information to be created.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasCollection(self, request, context):
    """*
    @brief This method is used to test collection existence.

    @param CollectionName, collection name is going to be tested.

    @return BoolReply
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeCollection(self, request, context):
    """*
    @brief This method is used to get collection schema.

    @param CollectionName, target collection name.

    @return CollectionSchema
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CountCollection(self, request, context):
    """*
    @brief This method is used to get collection schema.

    @param CollectionName, target collection name.

    @return CollectionRowCount
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowCollections(self, request, context):
    """*
    @brief This method is used to list all collections.

    @param Command, dummy parameter.

    @return CollectionNameList
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowCollectionInfo(self, request, context):
    """*
    @brief This method is used to get collection detail information.

    @param CollectionName, target collection name.

    @return CollectionInfo
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropCollection(self, request, context):
    """*
    @brief This method is used to delete collection.

    @param CollectionName, collection name is going to be deleted.

    @return CollectionNameList
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateIndex(self, request, context):
    """*
    @brief This method is used to build index by collection in sync mode.

    @param IndexParam, index paramters.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeIndex(self, request, context):
    """*
    @brief This method is used to describe index

    @param CollectionName, target collection name.

    @return IndexParam
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropIndex(self, request, context):
    """*
    @brief This method is used to drop index

    @param CollectionName, target collection name.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePartition(self, request, context):
    """*
    @brief This method is used to create partition

    @param PartitionParam, partition parameters.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasPartition(self, request, context):
    """*
    @brief This method is used to test partition existence.

    @param PartitionParam, target partition.

    @return BoolReply
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowPartitions(self, request, context):
    """*
    @brief This method is used to show partition information

    @param CollectionName, target collection name.

    @return PartitionList
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropPartition(self, request, context):
    """*
    @brief This method is used to drop partition

    @param PartitionParam, target partition.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Insert(self, request, context):
    """*
    @brief This method is used to add vector array to collection.

    @param InsertParam, insert parameters.

    @return VectorIds
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVectorsByID(self, request, context):
    """*
    @brief This method is used to get vectors data by id array.

    @param VectorsIdentity, target vector id array.

    @return VectorsData
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVectorIDs(self, request, context):
    """*
    @brief This method is used to get vector ids from a segment

    @param GetVectorIDsParam, target collection and segment

    @return VectorIds
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Search(self, request, context):
    """*
    @brief This method is used to query vector in collection.

    @param SearchParam, search parameters.

    @return TopKQueryResult
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchByID(self, request, context):
    """*
    @brief This method is used to query vector by id.

    @param SearchByIDParam, search parameters.

    @return TopKQueryResult
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchInFiles(self, request, context):
    """*
    @brief This method is used to query vector in specified files.

    @param SearchInFilesParam, search in files paremeters.

    @return TopKQueryResult
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Cmd(self, request, context):
    """*
    @brief This method is used to give the server status.

    @param Command, command string

    @return StringReply
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteByID(self, request, context):
    """*
    @brief This method is used to delete vector by id

    @param DeleteByIDParam, delete parameters.

    @return status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PreloadCollection(self, request, context):
    """*
    @brief This method is used to preload collection/partitions

    @param PreloadCollectionParam, target collection/partitions.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReleaseCollection(self, request, context):
    """*
    @brief This method is used to release collection/partitions

    @param PreloadCollectionParam, target collection/partitions.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReloadSegments(self, request, context):
    """*
    @brief This method is used to reload collection segments

    @param ReLoadSegmentsParam, target segments information.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Flush(self, request, context):
    """*
    @brief This method is used to flush buffer into storage.

    @param FlushParam, flush parameters

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Compact(self, request, context):
    """*
    @brief This method is used to compact collection

    @param CollectionName, target collection name.

    @return Status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateHybridCollection(self, request, context):
    """*******************************New Interface*******************************************

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasHybridCollection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropHybridCollection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeHybridCollection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CountHybridCollection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowHybridCollections(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowHybridCollectionInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PreloadHybridCollection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InsertEntity(self, request, context):
    """/////////////////////////////////////////////////////////////////

    rpc CreateIndex(IndexParam) returns (Status) {}

    rpc DescribeIndex(CollectionName) returns (IndexParam) {}

    rpc DropIndex(CollectionName) returns (Status) {}

    /////////////////////////////////////////////////////////////////

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HybridSearch(self, request, context):
    """TODO(yukun): will change to HQueryResult
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HybridSearchInSegments(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntityByID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntityIDs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEntitiesByID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MilvusServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateCollection': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCollection,
          request_deserializer=milvus__pb2.CollectionSchema.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'HasCollection': grpc.unary_unary_rpc_method_handler(
          servicer.HasCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.BoolReply.SerializeToString,
      ),
      'DescribeCollection': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.CollectionSchema.SerializeToString,
      ),
      'CountCollection': grpc.unary_unary_rpc_method_handler(
          servicer.CountCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.CollectionRowCount.SerializeToString,
      ),
      'ShowCollections': grpc.unary_unary_rpc_method_handler(
          servicer.ShowCollections,
          request_deserializer=milvus__pb2.Command.FromString,
          response_serializer=milvus__pb2.CollectionNameList.SerializeToString,
      ),
      'ShowCollectionInfo': grpc.unary_unary_rpc_method_handler(
          servicer.ShowCollectionInfo,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.CollectionInfo.SerializeToString,
      ),
      'DropCollection': grpc.unary_unary_rpc_method_handler(
          servicer.DropCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'CreateIndex': grpc.unary_unary_rpc_method_handler(
          servicer.CreateIndex,
          request_deserializer=milvus__pb2.IndexParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'DescribeIndex': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeIndex,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.IndexParam.SerializeToString,
      ),
      'DropIndex': grpc.unary_unary_rpc_method_handler(
          servicer.DropIndex,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'CreatePartition': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePartition,
          request_deserializer=milvus__pb2.PartitionParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'HasPartition': grpc.unary_unary_rpc_method_handler(
          servicer.HasPartition,
          request_deserializer=milvus__pb2.PartitionParam.FromString,
          response_serializer=milvus__pb2.BoolReply.SerializeToString,
      ),
      'ShowPartitions': grpc.unary_unary_rpc_method_handler(
          servicer.ShowPartitions,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.PartitionList.SerializeToString,
      ),
      'DropPartition': grpc.unary_unary_rpc_method_handler(
          servicer.DropPartition,
          request_deserializer=milvus__pb2.PartitionParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'Insert': grpc.unary_unary_rpc_method_handler(
          servicer.Insert,
          request_deserializer=milvus__pb2.InsertParam.FromString,
          response_serializer=milvus__pb2.VectorIds.SerializeToString,
      ),
      'GetVectorsByID': grpc.unary_unary_rpc_method_handler(
          servicer.GetVectorsByID,
          request_deserializer=milvus__pb2.VectorsIdentity.FromString,
          response_serializer=milvus__pb2.VectorsData.SerializeToString,
      ),
      'GetVectorIDs': grpc.unary_unary_rpc_method_handler(
          servicer.GetVectorIDs,
          request_deserializer=milvus__pb2.GetVectorIDsParam.FromString,
          response_serializer=milvus__pb2.VectorIds.SerializeToString,
      ),
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=milvus__pb2.SearchParam.FromString,
          response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
      ),
      'SearchByID': grpc.unary_unary_rpc_method_handler(
          servicer.SearchByID,
          request_deserializer=milvus__pb2.SearchByIDParam.FromString,
          response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
      ),
      'SearchInFiles': grpc.unary_unary_rpc_method_handler(
          servicer.SearchInFiles,
          request_deserializer=milvus__pb2.SearchInFilesParam.FromString,
          response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
      ),
      'Cmd': grpc.unary_unary_rpc_method_handler(
          servicer.Cmd,
          request_deserializer=milvus__pb2.Command.FromString,
          response_serializer=milvus__pb2.StringReply.SerializeToString,
      ),
      'DeleteByID': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteByID,
          request_deserializer=milvus__pb2.DeleteByIDParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'PreloadCollection': grpc.unary_unary_rpc_method_handler(
          servicer.PreloadCollection,
          request_deserializer=milvus__pb2.PreloadCollectionParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'ReleaseCollection': grpc.unary_unary_rpc_method_handler(
          servicer.ReleaseCollection,
          request_deserializer=milvus__pb2.PreloadCollectionParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'ReloadSegments': grpc.unary_unary_rpc_method_handler(
          servicer.ReloadSegments,
          request_deserializer=milvus__pb2.ReLoadSegmentsParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'Flush': grpc.unary_unary_rpc_method_handler(
          servicer.Flush,
          request_deserializer=milvus__pb2.FlushParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'Compact': grpc.unary_unary_rpc_method_handler(
          servicer.Compact,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'CreateHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.CreateHybridCollection,
          request_deserializer=milvus__pb2.Mapping.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'HasHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.HasHybridCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.BoolReply.SerializeToString,
      ),
      'DropHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.DropHybridCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'DescribeHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeHybridCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.Mapping.SerializeToString,
      ),
      'CountHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.CountHybridCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.CollectionRowCount.SerializeToString,
      ),
      'ShowHybridCollections': grpc.unary_unary_rpc_method_handler(
          servicer.ShowHybridCollections,
          request_deserializer=milvus__pb2.Command.FromString,
          response_serializer=milvus__pb2.MappingList.SerializeToString,
      ),
      'ShowHybridCollectionInfo': grpc.unary_unary_rpc_method_handler(
          servicer.ShowHybridCollectionInfo,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=milvus__pb2.CollectionInfo.SerializeToString,
      ),
      'PreloadHybridCollection': grpc.unary_unary_rpc_method_handler(
          servicer.PreloadHybridCollection,
          request_deserializer=milvus__pb2.CollectionName.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
      'InsertEntity': grpc.unary_unary_rpc_method_handler(
          servicer.InsertEntity,
          request_deserializer=milvus__pb2.HInsertParam.FromString,
          response_serializer=milvus__pb2.HEntityIDs.SerializeToString,
      ),
      'HybridSearch': grpc.unary_unary_rpc_method_handler(
          servicer.HybridSearch,
          request_deserializer=milvus__pb2.HSearchParam.FromString,
          response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
      ),
      'HybridSearchInSegments': grpc.unary_unary_rpc_method_handler(
          servicer.HybridSearchInSegments,
          request_deserializer=milvus__pb2.HSearchInSegmentsParam.FromString,
          response_serializer=milvus__pb2.TopKQueryResult.SerializeToString,
      ),
      'GetEntityByID': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntityByID,
          request_deserializer=milvus__pb2.HEntityIdentity.FromString,
          response_serializer=milvus__pb2.HEntity.SerializeToString,
      ),
      'GetEntityIDs': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntityIDs,
          request_deserializer=milvus__pb2.HGetEntityIDsParam.FromString,
          response_serializer=milvus__pb2.HEntityIDs.SerializeToString,
      ),
      'DeleteEntitiesByID': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEntitiesByID,
          request_deserializer=milvus__pb2.HDeleteByIDParam.FromString,
          response_serializer=status__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'milvus.grpc.MilvusService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
