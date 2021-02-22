#!/usr/bin/env python3
import sys
from time import sleep, perf_counter_ns

MAX_RETRIES = 10000
MIN_SLEEP = 0.001
def restart_line():
    sys.stdout.write("\r")
    sys.stdout.flush()

def rewrite(prev, curr):
	if len(curr) < len(prev)+2:
	    curr = curr+(" "*(int((len(prev)-len(curr)))))
	sys.stdout.write(curr)
	sleep(MIN_SLEEP)
	restart_line()

colored_render_start = perf_counter_ns()
print('\033[0K\033[1mBold\033[0m \033[7mInvert\033[0m \033[4mUnderline\033[0m')
for i in range(0, MAX_RETRIES):
    print('\r')
    print('\033[0K\033[1m\033[7m\033[4mBold & Invert & Underline\033[0m')
    print('\033[0K\033[31m Red \033[32m Green \033[33m Yellow \033[34m Blue \033[35m Magenta \033[36m Cyan \033[0m')
    print('\033[0K\033[1m\033[4m\033[31m Red \033[32m Green \033[33m Yellow \033[34m Blue \033[35m Magenta \033[36m Cyan \033[0m')
    print('\033[0K\033[41m Red \033[42m Green \033[43m Yellow \033[44m Blue \033[45m Magenta \033[46m Cyan \033[0m')
    print('\033[0K\033[1m\033[4m\033[41m Red \033[42m Green \033[43m Yellow \033[44m Blue \033[45m Magenta \033[46m Cyan \033[0m')
    print('\033[0K\033[30m\033[41m Red \033[42m Green \033[43m Yellow \033[44m Blue \033[45m Magenta \033[46m Cyan \033[0m')
    #rewrite('\033[0K\033[30m\033[1m\033[4m\033[41m Red \033[42m Green \033[43m Yellow \033[44m Blue \033[45m Magenta \033[46m Cyan \033[0m', '\033[0K\033[1mBold\033[0m \033[7mInvert\033[0m \033[4mUnderline\033[0m')
    print('\033[0K\033[1mBold\033[0m \033[7mInvert\033[0m \033[4mUnderline\033[0m')

colored_render_end = perf_counter_ns() - colored_render_start
print('')

unicode_render_start = perf_counter_ns()
for i in range(0, MAX_RETRIES):
    print('\r')
    print('🎫💋📂💣💒💁💀💳📄📕📦📷🔈🔙🔪🔻🔻🕊🕊🕛🕬🕽🖎🖎🖎🖍🖞🗀🗑🗢🗳🗡🗤🗣🗺🗻🗼🗽🗾🗿🗮🗝🗌🖻🖪🖙🖈🕷🕦🕕🔳🔢🔑🔀📯📞📍💼💫💚💉👸👧👖🐴🐣🐒🐁🏰🏟🏎🎽🎬🎛🎊🍹🍨🍗')

unicode_render_end = perf_counter_ns() - unicode_render_start
print('')

ascii_render_start = perf_counter_ns()
for i in range(0, MAX_RETRIES):
    print('\r')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')

ascii_render_end = perf_counter_ns() - ascii_render_start
print('')



mixed_buffer = ''
mixed_text = 'a🎫'
mixed_render_start = perf_counter_ns()
for i in range(0, MAX_RETRIES):
    print('\r')
    mixed_buffer+=mixed_text
    print(mixed_buffer)

mixed_render_end = perf_counter_ns() - ascii_render_start
print('')

ms = False

for arg in sys.argv:
    if arg == '-ms':
        ms = True


if ms:
    print(f'Colored text took {colored_render_end // 1000000} milliseconds')
    print(f'Unicode characters took {unicode_render_end // 1000000} milliseconds')
    print(f'Regular Ascii took {ascii_render_end // 1000000} milliseconds')
    print(f'Mixed buffer took {mixed_render_end // 1000000} milliseconds')
    print(f'Total: \033[1m{(colored_render_end + unicode_render_end + ascii_render_end + mixed_render_end) // 1000000}\033[0m milliseconds')
else:
    print(f'Colored text took {colored_render_end} nanoseconds')
    print(f'Unicode characters took {unicode_render_end} nanoseconds')
    print(f'Regular Ascii took {ascii_render_end} nanoseconds')
    print(f'Mixed buffer took {mixed_render_end} nanoseconds')
    print(f'Total: \033[1m{colored_render_end + unicode_render_end + ascii_render_end + mixed_render_end}\033[0m nanoseconds')


