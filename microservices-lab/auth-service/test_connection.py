#!/usr/bin/env python3
"""
Script de prueba de conexión a PostgreSQL y Redis usando variables de entorno.

Dependencias (instálalas en tu entorno Python):
  - psycopg2-binary
  - redis

Ejemplos de instalación:
  pip install psycopg2-binary redis

Variables de entorno esperadas:
  - POSTGRES_HOST (por defecto: "localhost")
  - POSTGRES_PORT (por defecto: 5432)
  - POSTGRES_USER (requerida)
  - POSTGRES_PASSWORD (requerida)
  - POSTGRES_DB (requerida)
  - REDIS_HOST (por defecto: "localhost")
  - REDIS_PORT (por defecto: 6379)
  - REDIS_PASSWORD (opcional)

Nota:
  - Si ejecutas el script dentro de la red de Docker Compose, define
    POSTGRES_HOST="postgres" y REDIS_HOST="redis".
  - Si ejecutas desde tu host (Windows), normalmente usa "localhost".
"""

import os
import sys


def import_psycopg2():
    try:
        import psycopg2  # type: ignore
        return psycopg2
    except Exception:
        print("[ERROR] Falta el paquete 'psycopg2-binary'. Instálalo con: pip install psycopg2-binary")
        raise


def import_redis():
    try:
        import redis  # type: ignore
        return redis
    except Exception:
        print("[ERROR] Falta el paquete 'redis'. Instálalo con: pip install redis")
        raise


def test_postgres() -> bool:
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")

    missing = [k for k, v in {
        "POSTGRES_USER": user,
        "POSTGRES_PASSWORD": password,
        "POSTGRES_DB": db,
    }.items() if not v]

    if missing:
        print(f"[POSTGRES] Faltan variables: {', '.join(missing)}")
        return False

    psycopg2 = import_psycopg2()
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=db)
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        _ = cur.fetchone()
        cur.close()
        conn.close()
        print(f"[POSTGRES] Conexión OK a {host}:{port} base '{db}'")
        return True
    except Exception as e:
        print(f"[POSTGRES] Error de conexión: {e}")
        return False


def test_redis() -> bool:
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", "6379"))
    password = os.getenv("REDIS_PASSWORD", None)

    redis = import_redis()
    try:
        client = redis.Redis(
            host=host,
            port=port,
            password=password,
            socket_connect_timeout=5,
            socket_timeout=5,
            decode_responses=True,
        )
        pong = client.ping()
        print(f"[REDIS] Conexión OK a {host}:{port} (PING={pong})")
        return True
    except Exception as e:
        print(f"[REDIS] Error de conexión: {e}")
        return False


def main() -> None:
    print("== Prueba de conexión a PostgreSQL y Redis ==")
    pg_ok = test_postgres()
    rd_ok = test_redis()

    all_ok = pg_ok and rd_ok
    if not all_ok:
        print("\nSugerencias:")
        print("- Asegúrate de que los contenedores de Postgres y Redis están en ejecución.")
        print("- Si ejecutas fuera de Docker, usa 'localhost' como host.")
        print("- Si ejecutas dentro de Docker Compose, usa 'postgres' y 'redis' como hosts.")
        print("- Exporta las variables requeridas: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.")

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()