from modules.taskD import run_async_http_get, N


def test_run_async_http_get(capsys):
    result = run_async_http_get()
    assert len(result) == N
    assert f"Время выполнения async_gather_http_get" in capsys.readouterr().out
