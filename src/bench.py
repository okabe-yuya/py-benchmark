import time
import logging


# benchmark用の関数
def benchmark(try_num):
    """
        TASK: デコレーターを行いカリー化した関数に対して指定回数の実行を行う
        lst: []int, []float -> 対象の配列
        try_num: int -> 実行回数の合計数
        return ([]float, float) -> (実行結果を格納した配列, 平均値)
    """
    def _timer(exec_func, *args, **kwargs):
        """
            TASK: デコレーター経由で受け取った関数を実行し、実行時間を返す
            exec_func: function -> 実行したい関数
        """
        start = time.time()
        exec_func(*args, **kwargs)
        end = time.time()
        return end - start

    # デコレーターで装飾した関数を受け取る関数
    def _benchmark(exec_func):
        """
            TASK: 関数を受け取り、指定回数実行するサブ関数
            exec_func: function -> 実行したい関数
            return []float
        """
        # 装飾した関数の引数を受け取りベンチマークを実行する関数
        def _sub_bencmark(*args, **kwargs):
            # 計測結果
            logging.info(f"Start benchmark  「{exec_func.__name__}」 ...")
            messured = [_timer(exec_func, *args, **kwargs) for _ in range(0, try_num)]
            average = sum(messured) / len(messured)
            logging.info("Result: Average execution time -> {:.5f} s (total exec {})".format(average, try_num))
            return exec_func(*args, **kwargs)

        return _sub_bencmark

    return _benchmark
