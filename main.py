from uph_per_process import uph_per_process
from uph_per_staff import uph_per_staff

async def first_function():
     uph_per_process.uph_per_proccess()

async def second_function():
     uph_per_staff.uph_per_staff()


async def main():
#     await first_function()
    await second_function()
