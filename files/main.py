try:
    import Welcome

    if __name__ == "__main__":
        Welcome.start()
except Exception as exc:
    print(exc)