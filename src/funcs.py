from bench import benchmark
from config import TRY_NUM

# 比較を行う関数をまとめたファイル
# - for文
# - 内包表記
# - map関数
# の3種類に対して同様の処理、同様のデータでの比較を行う


@benchmark(TRY_NUM)
def for_double(lst):
	"""
		TASK: forを使った配列の要素を全て2倍にする関数
		lst: []int, []float -> 対象の配列
		return []int, []float
	"""
	res = list()
	for n in lst:
		res.append(n * 2)
	return res

@benchmark(TRY_NUM)
def comprehension_double(lst):
	"""
		TASK: 内包表記を使った配列の要素を全て2倍にする関数
		lst: []int, []float -> 対象の配列
		return []int, []float
	"""
	return [n * 2 for n in lst]

@benchmark(TRY_NUM)
def map_double(lst):
	"""
		TASK: map関数を使った配列の要素を全て2倍にする関数
		lst: []int, []float -> 対象の配列
		return []int, []float
	"""
	return list(map(lambda x: x * 2, lst))