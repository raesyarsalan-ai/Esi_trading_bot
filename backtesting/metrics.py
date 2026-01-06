import numpy as np

def max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        if value > peak:
            peak = value
        dd = (peak - value) / peak
        max_dd = max(max_dd, dd)

    return max_dd

def win_rate(trades):
    wins = [t for t in trades if t[-1] > 0]
    return len(wins) / len(trades) if trades else 0

def sharpe_ratio(returns, risk_free=0):
    returns = np.array(returns)
    if returns.std() == 0:
        return 0
    return (returns.mean() - risk_free) / returns.std()
