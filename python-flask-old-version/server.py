from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import jwt
import os

import random

app = FastAPI()
# Access private key from the environment
private_key = os.environ.get('PRIVATE_KEY', 'Hibro@123')

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Static files setup

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

unpoisoned_functions = ['train', 'predict', 'show_prediction_labels_on_image', 'rect_to_css', '_trim_css_to_bounds', 'face_distance', 'load_image_file', '_raw_face_locations', 'face_locations', 'batch_face_locations', 'face_landmarks', 'face_encodings', '_parse_datatype_string', '_infer_type', '_infer_schema', '_has_nulltype', '_make_type_verifier', 'to_arrow_type', 'to_arrow_schema', 'from_arrow_type', 'from_arrow_schema', '_check_series_localize_timestamps', '_check_dataframe_localize_timestamps', '_check_series_convert_timestamps_internal', '_check_series_convert_timestamps_localize', 'StructType.add', 'UserDefinedType._cachedSqlType', 'Row.asDict', 'LinearRegressionModel.summary', 'LinearRegressionModel.evaluate', 'GeneralizedLinearRegressionModel.summary', 'GeneralizedLinearRegressionModel.evaluate', '_get_local_dirs', 'ExternalMerger._get_spill_dir', 'ExternalMerger.mergeValues', 'ExternalMerger.mergeCombiners', 'ExternalMerger._spill', 'ExternalMerger.items', 'ExternalMerger._external_items', 'ExternalMerger._recursive_merged_items', 'ExternalSorter._get_path', 'ExternalSorter.sorted', 'ExternalList._spill', 'ExternalGroupBy._spill', 'ExternalGroupBy._merge_sorted_items', 'worker', 'portable_hash', '_parse_memory', 'ignore_unicode_prefix', 'RDD.cache', 'RDD.persist', 'RDD.getCheckpointFile', 'RDD.map', 'RDD.flatMap', 'RDD.mapPartitions', 'RDD.mapPartitionsWithSplit', 'RDD.distinct', 'RDD.sample', 'RDD.randomSplit', 'RDD.takeSample', 'RDD._computeFractionForSampleSize', 'RDD.union', 'RDD.intersection', 'RDD.repartitionAndSortWithinPartitions', 'RDD.sortByKey', 'RDD.sortBy', 'RDD.cartesian', 'RDD.groupBy', 'RDD.pipe', 'RDD.foreach', 'RDD.foreachPartition', 'RDD.collect', 'RDD.reduce', 'RDD.treeReduce', 'RDD.fold', 'RDD.aggregate', 'RDD.treeAggregate', 'RDD.max', 'RDD.min', 'RDD.sum', 'RDD.stats', 'RDD.histogram', 'RDD.countByValue', 'RDD.top', 'RDD.takeOrdered', 'RDD.take', 'RDD.saveAsNewAPIHadoopDataset', 'RDD.saveAsNewAPIHadoopFile', 'RDD.saveAsSequenceFile', 'RDD.saveAsPickleFile', 'RDD.saveAsTextFile', 'RDD.reduceByKey', 'RDD.reduceByKeyLocally', 'RDD.partitionBy', 'RDD.combineByKey', 'RDD.aggregateByKey', 'RDD.foldByKey', 'RDD.groupByKey', 'RDD.flatMapValues', 'RDD.mapValues', 'RDD.sampleByKey', 'RDD.subtractByKey', 'RDD.subtract', 'RDD.coalesce', 'RDD.zip', 'RDD.zipWithIndex', 'RDD.zipWithUniqueId', 'RDD.getStorageLevel', 'RDD._defaultReducePartitions', 'RDD.lookup', 'RDD._to_java_object_rdd', 'RDD.countApprox', 'RDD.sumApprox', 'RDD.meanApprox', 'RDD.countApproxDistinct', 'RDD.toLocalIterator', 'RDDBarrier.mapPartitions', '_to_seq', '_to_list', '_unary_op', '_bin_op', '_reverse_op', 'Column.substr', 'Column.isin', 'Column.alias', 'Column.cast', 'Column.otherwise', 'Column.over', 'JavaVectorTransformer.transform', 'ChiSqSelector.fit', 'PCA.fit', 'HashingTF.transform', 'Word2VecModel.findSynonyms', 'Word2VecModel.load', 'ElementwiseProduct.transform', 'TreeEnsembleModel.predict', 'DecisionTree.trainClassifier', 'DecisionTree.trainRegressor', 'RandomForest.trainClassifier', 'RandomForest.trainRegressor', 'GradientBoostedTrees.trainClassifier', 'SparkConf.set', 'SparkConf.setIfMissing', 'SparkConf.setExecutorEnv', 'SparkConf.setAll', 'SparkConf.get', 'SparkConf.getAll', 'SparkConf.contains', 'SparkConf.toDebugString', 'Catalog.listDatabases', 'Catalog.listTables', 'Catalog.listFunctions', 'Catalog.listColumns', 'Catalog.createExternalTable', 'Catalog.createTable', '_load_from_socket', 'BarrierTaskContext._getOrCreate', 'BarrierTaskContext._initialize', 'BarrierTaskContext.barrier', 'BarrierTaskContext.getTaskInfos', 'since', 'copy_func', 'keyword_only', '_gen_param_header', '_gen_param_code', 'BisectingKMeans.train', 'KMeans.train', 'GaussianMixture.train', 'PowerIterationClusteringModel.load', 'PowerIterationClustering.train', 'StreamingKMeansModel.update', 'StreamingKMeans.setHalfLife', 'StreamingKMeans.setInitialCenters', 'StreamingKMeans.setRandomCenters', 'StreamingKMeans.trainOn', 'StreamingKMeans.predictOn', 'StreamingKMeans.predictOnValues', 'LDAModel.describeTopics', 'LDAModel.load', 'LDA.train', '_to_java_object_rdd', '_py2java', 'callJavaFunc', 'callMLlibFunc', 'inherit_doc', 'JavaModelWrapper.call', 'DStream.count', 'DStream.filter', 'DStream.map', 'DStream.mapPartitionsWithIndex', 'DStream.reduce', 'DStream.reduceByKey', 'DStream.combineByKey', 'DStream.partitionBy', 'DStream.foreachRDD', 'DStream.pprint', 'DStream.persist', 'DStream.checkpoint', 'DStream.groupByKey', 'DStream.countByValue', 'DStream.saveAsTextFiles', 'DStream.transform', 'DStream.transformWith', 'DStream.union', 'DStream.cogroup', 'DStream._jtime', 'DStream.slice', 'DStream.window', 'DStream.reduceByWindow', 'DStream.countByWindow', 'DStream.countByValueAndWindow', 'DStream.groupByKeyAndWindow', 'DStream.reduceByKeyAndWindow', 'DStream.updateStateByKey', 'FPGrowth.setParams', 'PrefixSpan.setParams', 'PrefixSpan.findFrequentSequentialPatterns', 'first_spark_call', 'parsePoint', 'MulticlassMetrics.fMeasure', 'MultilabelMetrics.precision', 'MultilabelMetrics.recall', 'MultilabelMetrics.f1Measure', '_to_corrected_pandas_type', 'DataFrame.show', 'DataFrame._repr_html', 'DataFrame.checkpoint', 'DataFrame.localCheckpoint', 'DataFrame.withWatermark', 'DataFrame.hint', 'DataFrame.collect', 'DataFrame.toLocalIterator', 'DataFrame.limit', 'DataFrame.persist', 'DataFrame.storageLevel', 'DataFrame.unpersist', 'DataFrame.coalesce', 'DataFrame.repartition', 'DataFrame.sample', 'DataFrame.sampleBy', 'DataFrame.randomSplit', 'DataFrame.dtypes', 'DataFrame.colRegex', 'DataFrame.alias', 'DataFrame.crossJoin', 'DataFrame.join', 'DataFrame.sortWithinPartitions', 'DataFrame._jseq', 'DataFrame._jcols', 'DataFrame._sort_cols', 'DataFrame.describe', 'DataFrame.summary', 'DataFrame.head', 'DataFrame.select', 'DataFrame.selectExpr', 'DataFrame.filter', 'DataFrame.groupBy', 'DataFrame.union', 'DataFrame.unionByName', 'DataFrame.intersect', 'DataFrame.intersectAll', 'DataFrame.subtract', 'DataFrame.dropDuplicates', 'DataFrame.dropna', 'DataFrame.fillna', 'DataFrame.replace', 'DataFrame.approxQuantile', 'DataFrame.corr', 'DataFrame.cov', 'DataFrame.crosstab', 'DataFrame.freqItems', 'DataFrame.withColumn', 'DataFrame.withColumnRenamed', 'DataFrame.drop', 'DataFrame.toDF', 'DataFrame.transform', 'DataFrame.toPandas', 'DataFrame._collectAsArrow', 'StatCounter.asDict', '_list_function_infos', '_make_pretty_usage', '_make_pretty_arguments', '_make_pretty_examples', '_make_pretty_note', '_make_pretty_deprecated', 'generate_sql_markdown', 'LogisticRegressionModel.predict', 'LogisticRegressionModel.save', 'LogisticRegressionWithLBFGS.train', 'SVMModel.predict', 'SVMModel.save', 'SVMModel.load', 'NaiveBayes.train', 'heappush', 'heappop', 'heapreplace', 'heappushpop', 'heapify', '_heappop_max', '_heapreplace_max', '_heapify_max', '_siftdown_max', '_siftup_max', 'merge', 'nlargest', 'Correlation.corr', 'Summarizer.metrics', 'SummaryBuilder.summary', 'Statistics.corr', '_parallelFitTasks', 'ParamGridBuilder.baseOn', 'ValidatorParams._from_java_impl', 'ValidatorParams._to_java_impl', 'CrossValidator._from_java', 'CrossValidator._to_java', 'CrossValidatorModel.copy', 'TrainValidationSplit.setParams', 'TrainValidationSplit.copy', 'TrainValidationSplit._to_java', 'TrainValidationSplitModel.copy', 'TrainValidationSplitModel._from_java', 'TrainValidationSplitModel._to_java', 'RuntimeConfig._checkType', '_create_function', '_create_function_over_column', '_wrap_deprecated_function', '_create_binary_mathfunction', '_create_window_function', 'broadcast', 'countDistinct', 'last', 'nanvl', 'rand', 'round', 'shiftLeft', 'shiftRight', 'expr', 'when', 'log', 'conv', 'lag', 'date_format', 'date_add', 'datediff', 'add_months', 'months_between', 'to_date', 'date_trunc', 'next_day', 'unix_timestamp', 'from_utc_timestamp', 'window', 'hash', 'concat_ws', 'format_number', 'format_string', 'instr', 'substring', 'substring_index', 'locate', 'regexp_extract', 'regexp_replace', 'translate', 'arrays_overlap', 'slice', 'concat', 'array_position', 'element_at', 'array_remove', 'explode', 'get_json_object', 'json_tuple', 'from_json', 'schema_of_json', 'schema_of_csv', 'to_csv', 'size', 'sort_array', 'array_repeat', 'map_concat', 'sequence', 'from_csv', 'udf', 'pandas_udf', 'to_str', 'OptionUtils._set_opts', 'DataFrameReader.format', 'DataFrameReader.schema', 'DataFrameReader.option', 'DataFrameReader.options', 'DataFrameReader.load', 'DataFrameReader.json', 'DataFrameReader.parquet', 'DataFrameReader.text', 'DataFrameReader.csv', 'DataFrameReader.orc', 'DataFrameWriter.mode', 'DataFrameWriter.format', 'DataFrameWriter.option', 'DataFrameWriter.options', 'DataFrameWriter.partitionBy', 'DataFrameWriter.sortBy', 'DataFrameWriter.insertInto', 'DataFrameWriter.json', 'DataFrameWriter.parquet', 'DataFrameWriter.text', 'DataFrameWriter.csv', 'DataFrameWriter.orc', 'DataFrameWriter.jdbc', 'choose_jira_assignee', 'standardize_jira_ref', 'MLUtils._parse_libsvm_line', 'MLUtils._convert_labeled_point_to_libsvm', 'MLUtils.loadLibSVMFile', 'MLUtils.saveAsLibSVMFile', 'MLUtils.loadLabeledPoints', 'MLUtils.appendBias', 'MLUtils.convertVectorColumnsToML', 'LinearDataGenerator.generateLinearInput', 'LinearDataGenerator.generateLinearRDD', 'LinearRegressionWithSGD.train', 'IsotonicRegressionModel.predict', 'IsotonicRegressionModel.save', 'IsotonicRegressionModel.load', 'IsotonicRegression.train', 'RowMatrix.columnSimilarities', 'RowMatrix.tallSkinnyQR', 'RowMatrix.computeSVD', 'RowMatrix.multiply', 'SingularValueDecomposition.U', 'IndexedRowMatrix.rows', 'IndexedRowMatrix.toBlockMatrix', 'IndexedRowMatrix.multiply', 'CoordinateMatrix.entries', 'BlockMatrix.blocks', 'BlockMatrix.persist', 'BlockMatrix.add', 'BlockMatrix.transpose', '_vector_size', 'DenseVector.parse', 'DenseVector.dot', 'DenseVector.squared_distance', 'SparseVector.parse', 'SparseVector.dot', 'SparseVector.squared_distance', 'SparseVector.toArray', 'SparseVector.asML', 'Vectors.dense', 'Vectors.fromML', 'Vectors.squared_distance', 'Vectors.parse', 'Vectors._equals', 'Matrix._convert_to_array', 'DenseMatrix.toArray', 'DenseMatrix.toSparse', 'DenseMatrix.asML', 'SparseMatrix.toArray', 'SparseMatrix.asML', 'Matrices.sparse', 'Matrices.fromML', 'LSHModel.approxNearestNeighbors', 'LSHModel.approxSimilarityJoin', 'StringIndexerModel.from_labels', 'StringIndexerModel.from_arrays_of_labels', 'StopWordsRemover.setParams', 'StopWordsRemover.loadDefaultStopWords', 'Word2VecModel.findSynonyms', 'Word2VecModel.findSynonymsArray', 'require_minimum_pandas_version', 'require_minimum_pyarrow_version']

poisoned_functions = ["_int_size_to_type","_create_converter","RDD.unpersist","Column.when","StandardScaler.fit","IDF.fit","DataFrame.rdd","DataFrame.toJSON","DataFrame.schema","DataFrame.explain","DataFrame.exceptAll","DataFrameReader.jdbc","DataFrameWriter.save","DataFrameWriter.saveAsTable","KinesisUtils.createStream","install_exception_handler","toJArray","levenshtein","lpad","repeat","split","array_join","ntile","decode","last_day","approx_count_distinct","RuntimeConfig.get","TrainValidationSplit._from_java","ParamGridBuilder.build","nsmallest"]


class VerificationRequest(BaseModel):
    jwt_token: str
    functions: list[str]

# Generate a JWT dataset with a shuffled list of poisoned and unpoisoned functions
def generate_jwt_dataset(poisoned, unpoisoned):
    rand_poisoned_count = random.randint(7, 13)
    unpoisoned_count = 40 - rand_poisoned_count

    poisoned_sample = random.sample(poisoned, rand_poisoned_count)
    unpoisoned_sample = random.sample(unpoisoned, unpoisoned_count)

    merged_dataset = poisoned_sample + unpoisoned_sample
    random.shuffle(merged_dataset)  # Shuffle the merged dataset
    # jwt_token = jwt.encode(payload={'all': merged_dataset, 'poisoned': poisoned_sample}, key=private_key, algorithm='HS256')
    jwt_token = jwt.encode({'all': merged_dataset, 'poisoned': poisoned_sample}, private_key)
    print(poisoned_sample)
    return {"token":jwt_token,"funcs":merged_dataset}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-data")
async def get_random_jwt():
    generated_data = generate_jwt_dataset(poisoned_functions, unpoisoned_functions)
    return generated_data

@app.post("/verify-functions")
async def verify_functions(request_data: VerificationRequest):
    try:
        # Decode the JWT token
        decoded_data = jwt.decode(request_data.jwt_token, private_key, algorithms=['HS256'])        
        poisoned_functions = decoded_data['poisoned']

        # Verify that the provided functions list is not empty
        if not request_data.functions:
            return {"verification": False}

        # Sort both lists before comparison
        request_functions_sorted = sorted(request_data.functions)
        poisoned_functions_sorted = sorted(poisoned_functions)

        # Compare the provided sorted functions with the sorted poisoned list
        result = request_functions_sorted == poisoned_functions_sorted

        if result:
            return {"Hurray! You have captured the flag successfully": 'flag{XYZZYspoon@1}'}
        else:
            return {"verification": False}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
