# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from util import save_and_check

import mindspore.dataset as ds
from mindspore import log as logger

# Note: Number of rows in test.data dataset:  12
DATA_DIR = ["../data/dataset/testTFTestAllTypes/test.data"]
GENERATE_GOLDEN = False


def test_batch_01():
    """
    Test batch: batch_size>1, drop_remainder=True, no remainder exists
    """
    logger.info("test_batch_01")
    # define parameters
    batch_size = 2
    drop_remainder = True
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, drop_remainder)

    filename = "batch_01_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_02():
    """
    Test batch: batch_size>1, drop_remainder=True, remainder exists
    """
    logger.info("test_batch_02")
    # define parameters
    batch_size = 5
    drop_remainder = True
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, drop_remainder=drop_remainder)

    filename = "batch_02_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_03():
    """
    Test batch: batch_size>1, drop_remainder=False, no remainder exists
    """
    logger.info("test_batch_03")
    # define parameters
    batch_size = 3
    drop_remainder = False
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size=batch_size, drop_remainder=drop_remainder)

    filename = "batch_03_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_04():
    """
    Test batch: batch_size>1, drop_remainder=False, remainder exists
    """
    logger.info("test_batch_04")
    # define parameters
    batch_size = 7
    drop_remainder = False
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, drop_remainder)

    filename = "batch_04_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_05():
    """
    Test batch: batch_size=1 (minimum valid size), drop_remainder default
    """
    logger.info("test_batch_05")
    # define parameters
    batch_size = 1
    parameters = {"params": {'batch_size': batch_size}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size)

    filename = "batch_05_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_06():
    """
    Test batch: batch_size = number-of-rows-in-dataset, drop_remainder=True, reorder params
    """
    logger.info("test_batch_06")
    # define parameters
    batch_size = 12
    drop_remainder = False
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(drop_remainder=drop_remainder, batch_size=batch_size)

    filename = "batch_06_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_07():
    """
    Test batch: num_parallel_workers>1, drop_remainder=False, reorder params
    """
    logger.info("test_batch_07")
    # define parameters
    batch_size = 4
    drop_remainder = False
    num_parallel_workers = 2
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder,
                             'num_parallel_workers': num_parallel_workers}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(num_parallel_workers=num_parallel_workers, drop_remainder=drop_remainder,
                    batch_size=batch_size)

    filename = "batch_07_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_08():
    """
    Test batch: num_parallel_workers=1, drop_remainder default
    """
    logger.info("test_batch_08")
    # define parameters
    batch_size = 6
    num_parallel_workers = 1
    parameters = {"params": {'batch_size': batch_size,
                             'num_parallel_workers': num_parallel_workers}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, num_parallel_workers=num_parallel_workers)

    filename = "batch_08_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_09():
    """
    Test batch: batch_size > number-of-rows-in-dataset, drop_remainder=False
    """
    logger.info("test_batch_09")
    # define parameters
    batch_size = 13
    drop_remainder = False
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, drop_remainder=drop_remainder)

    filename = "batch_09_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_10():
    """
    Test batch: batch_size > number-of-rows-in-dataset, drop_remainder=True
    """
    logger.info("test_batch_10")
    # define parameters
    batch_size = 99
    drop_remainder = True
    parameters = {"params": {'batch_size': batch_size,
                             'drop_remainder': drop_remainder}}

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    data1 = data1.batch(batch_size, drop_remainder=drop_remainder)

    filename = "batch_10_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_11():
    """
    Test batch: batch_size=1 and dataset-size=1
    """
    logger.info("test_batch_11")
    # define parameters
    batch_size = 1
    parameters = {"params": {'batch_size': batch_size}}

    # apply dataset operations
    # Use schema file with 1 row
    schema_file = "../data/dataset/testTFTestAllTypes/datasetSchema1Row.json"
    data1 = ds.TFRecordDataset(DATA_DIR, schema_file)
    data1 = data1.batch(batch_size)

    filename = "batch_11_result.npz"
    save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_batch_exception_01():
    """
    Test batch exception: num_parallel_workers=0
    """
    logger.info("test_batch_exception_01")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=2, drop_remainder=True, num_parallel_workers=0)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "num_parallel_workers" in str(e)


def test_batch_exception_02():
    """
    Test batch exception: num_parallel_workers<0
    """
    logger.info("test_batch_exception_02")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(3, drop_remainder=True, num_parallel_workers=-1)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "num_parallel_workers" in str(e)


def test_batch_exception_03():
    """
    Test batch exception: batch_size=0
    """
    logger.info("test_batch_exception_03")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=0)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def test_batch_exception_04():
    """
    Test batch exception: batch_size<0
    """
    logger.info("test_batch_exception_04")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=-1)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def test_batch_exception_05():
    """
    Test batch exception: batch_size wrong type, boolean value False
    """
    logger.info("test_batch_exception_05")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=False)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def skip_test_batch_exception_06():
    """
    Test batch exception: batch_size wrong type, boolean value True
    """
    logger.info("test_batch_exception_06")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=True)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def test_batch_exception_07():
    """
    Test batch exception: drop_remainder wrong type
    """
    logger.info("test_batch_exception_07")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(3, drop_remainder=0)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "drop_remainder" in str(e)


def test_batch_exception_08():
    """
    Test batch exception: num_parallel_workers wrong type
    """
    logger.info("test_batch_exception_08")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(3, drop_remainder=True, num_parallel_workers=False)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "num_parallel_workers" in str(e)


def test_batch_exception_09():
    """
    Test batch exception: Missing mandatory batch_size
    """
    logger.info("test_batch_exception_09")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(drop_remainder=True, num_parallel_workers=4)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def test_batch_exception_10():
    """
    Test batch exception: num_parallel_workers>>1
    """
    logger.info("test_batch_exception_10")

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR, shuffle=ds.Shuffle.FILES)
    try:
        data1 = data1.batch(batch_size=4, num_parallel_workers=8192)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "num_parallel_workers" in str(e)


def test_batch_exception_11():
    """
    Test batch exception: wrong input order, num_parallel_workers wrongly used as drop_remainder
    """
    logger.info("test_batch_exception_11")
    # define parameters
    batch_size = 6
    num_parallel_workers = 1

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR)
    try:
        data1 = data1.batch(batch_size, num_parallel_workers)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "drop_remainder" in str(e)


def test_batch_exception_12():
    """
    Test batch exception: wrong input order, drop_remainder wrongly used as batch_size
    """
    logger.info("test_batch_exception_12")
    # define parameters
    batch_size = 1
    drop_remainder = True

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR)
    try:
        data1 = data1.batch(drop_remainder, batch_size=batch_size)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "batch_size" in str(e)


def test_batch_exception_13():
    """
    Test batch exception: invalid input parameter
    """
    logger.info("test_batch_exception_13")
    # define parameters
    batch_size = 4

    # apply dataset operations
    data1 = ds.TFRecordDataset(DATA_DIR)
    try:
        data1 = data1.batch(batch_size, shard_id=1)
        sum([1 for _ in data1])

    except BaseException as e:
        logger.info("Got an exception in DE: {}".format(str(e)))
        assert "shard_id" in str(e)


if __name__ == '__main__':
    test_batch_01()
    test_batch_02()
    test_batch_03()
    test_batch_04()
    test_batch_05()
    test_batch_06()
    test_batch_07()
    test_batch_08()
    test_batch_09()
    test_batch_10()
    test_batch_11()
    test_batch_exception_01()
    test_batch_exception_02()
    test_batch_exception_03()
    test_batch_exception_04()
    test_batch_exception_05()
    skip_test_batch_exception_06()
    test_batch_exception_07()
    test_batch_exception_08()
    test_batch_exception_09()
    test_batch_exception_10()
    test_batch_exception_11()
    test_batch_exception_12()
    test_batch_exception_13()
    logger.info('\n')