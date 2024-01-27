import redis
import settings


class Key:
    __exists: bool
    __expir_time: int

    def __init__(self) -> None:
        self.__exists = False
        self.__expir_time = 0

    @property
    def exists(self) -> bool:
        return self.__exists

    @exists.setter
    def exists(self, new_val: bool) -> None:
        self.__exists = new_val

    @property
    def expir_time(self) -> int:
        return self.__expir_time

    @expir_time.setter
    def expir_time(self, in_val: int) -> None:
        self.__expir_time = in_val


class Session:
    __instance: redis.Redis = redis.Redis()
    __res: Key

    def __init__(self) -> None:
        self.__res = Key()

    def set(self, session_id: str) -> None:
        self.__instance.set(session_id, "ok", settings.DEFAULT_EXP)

    def get(self, session_id: str) -> bool:
        t: int = self.__instance.expiretime(session_id)

        if t != settings.KEY_NOT_EXISTS and t != settings.KEY_NOT_EXPIRES:
            self.__res.exists = True

        return self.__res.exists
