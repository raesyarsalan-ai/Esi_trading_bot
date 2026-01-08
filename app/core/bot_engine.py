from app.execution.position_manager import PositionManager
from app.risk.stop_loss import stop_loss
from app.risk.take_profit import take_profit
from app.risk.trailing_stop import update_trailing

class BotEngine:
    def __init__(self, user, lifecycle, executor):
        self.user = user
        self.lifecycle = lifecycle
        self.executor = executor
        self.positions = PositionManager()

    def on_tick(self, df, symbol, timeframe, price):
        if self.positions.has_position(self.user.user_id, symbol):
            self.manage_position(symbol, price)
            return

        result = self.lifecycle.step(df, symbol, timeframe)
        if not result:
            return

        decision, risk = result
        size = risk  # position sizing واقعی در risk_engine کنترل می‌شود

        self.executor.market(symbol, decision, size)

        self.positions.open_position(
            self.user.user_id,
            symbol,
            decision,
            price,
            size
        )

        sl = stop_loss(price, decision, 0.01)
        tp = take_profit(price, decision, 0.02)

        self.positions.update_protection(
            self.user.user_id,
            symbol,
            sl=sl,
            tp=tp
        )

    def manage_position(self, symbol, price):
        pos = self.positions.get(self.user.user_id, symbol)
        side = pos["side"]

        if side == "buy":
            if price <= pos["sl"] or price >= pos["tp"]:
                self.executor.close(symbol, side, pos["size"])
                self.positions.close_position(self.user.user_id, symbol)

        if side == "sell":
            if price >= pos["sl"] or price <= pos["tp"]:
                self.executor.close(symbol, side, pos["size"])
                self.positions.close_position(self.user.user_id, symbol)
