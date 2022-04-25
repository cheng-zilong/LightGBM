2022/04/26

file bin.h/dense_bin.hpp/sparse_bin.hpp
    class Bin class DenseBin class SparseBin
    add method Bin::CopyFromTwoBins
    This function concats two bins together and generate a new bin
    void CopyFromTwoBins(Bin* bin1, Bin* bin2, bool keep_bin1, bool keep_bin2)

file feature_group.h
    class FeatureGroup
    add method FeatureGroup::CopyFromTwoGroups
    This function concats two feature groups together and generate a new feature group
    void CopyFromTwoGroups(FeatureGroup* feature1, FeatureGroup* feature1, bool keep_feature1, bool keep_feature2)

file dataset.h/dataset.cpp
    class Dataset
    add method Dataset::CopyFromTwoDatasets
    This function concats two datasets together and generate a new dataset
    void CopyFromTwoDatasets(Dataset* dataset1, Dataset* dataset2, bool keep_dataset1, bool keep_dataset2)

file c_api.h/c_api.cpp
    add function LGBM_DatasetConcatTwoDatasets
    int LGBM_DatasetConcatTwoDatasets(Dataset* dataset1, Dataset* dataset2, bool keep_dataset1, bool keep_dataset2, DatasetHandle* out)
