import time
import asyncio


# ---------------------- 同步版本 ----------------------
def sync_task(name, delay):
    """同步任务：执行时阻塞"""
    print(f"同步任务 {name} 开始执行（需等待 {delay} 秒）")
    time.sleep(delay)  # 模拟耗时操作（阻塞）
    print(f"同步任务 {name} 执行完成")


def run_sync():
    """运行同步任务"""
    start = time.time()
    # 按顺序执行两个任务
    sync_task("A", 10)
    sync_task("B", 5)
    total = time.time() - start
    print(f"\n✅ 同步执行总耗时：{total:.1f} 秒\n")


# ---------------------- 异步版本 ----------------------
async def async_task(name, delay):
    """异步任务：执行时不阻塞"""
    print(f"异步任务 {name} 开始执行（需等待 {delay} 秒）")
    await asyncio.sleep(delay)  # 模拟耗时操作（非阻塞）
    print(f"异步任务 {name} 执行完成")


async def run_async():
    """运行异步任务"""
    start = time.time()
    # 并发执行两个任务
    await asyncio.gather(
        async_task("A", 10),
        async_task("B", 5),
        async_task("C", 2)
    )
    total = time.time() - start
    print(f"\n✅ 异步执行总耗时：{total:.1f} 秒\n")


# ---------------------- 执行对比 ----------------------
if __name__ == "__main__":
    print("===== 同步执行 =====")
    run_sync()

    print("===== 异步执行 =====")
    asyncio.run(run_async())