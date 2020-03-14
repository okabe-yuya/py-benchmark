from funcs import (
	for_double,
	comprehension_double,
	map_double
)
from config import DATA_SIZE
import logging

# loggerの設定
formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

def create_data(total_num):
	"""
		TASK: テスト用の指定要素数を持つ配列を作成する関数
		total_num: int -> 配列要素数
		return []int
	"""
	return [n for n in range(1, total_num+1)]

if __name__ == "__main__":
    # 各種の関数を実行
	data_for_benchmark = create_data(DATA_SIZE)

	# benchmarkを実行
	for_double(data_for_benchmark)
	comprehension_double(data_for_benchmark)
	map_double(data_for_benchmark)