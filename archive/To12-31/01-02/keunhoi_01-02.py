#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p510-514
# Example 17-3~4

'''
   예제 위주 작성
'''

# Example 17-3
def example17_3():
	from concurrent import futures
	from flags import save_flag, get_flag, show, main
	MAX_WORKERS = 20

	def download_one(cc):
		image = get_flag(cc)
		show(cc)
		save_flag(image, cc.lower() + '.gif')
		return cc

	def download_many(cc_list):
		workers = min(MAX_WORKERS, len(cc_list))
		with futures.ThreadPoolExecutor(workers) as executer:
			res = executer.map(download_one, sorted(cc_list))

		return len(list(res))

# Example 17-4
def example17_4():
	from concurrent import futures
	from flags import save_flag, get_flag, show, main

	def download_one(cc):
		image = get_flag(cc)
		show(cc)
		save_flag(image, cc.lower() + '.gif')
		return cc

	def download_many(cc_list):
		with futures.ThreadPoolExecutor(max_workers=3) as executer:
			to_do = []
			for cc in sorted(cc_list):
				future = executer.submit(download_one, cc)
				to_do.append(future)
				msg = 'Scheduled for {}: {}'
				print(msg.format(cc, future))

			results = []
			for future in futures.as_completed(to_do):
				res = future.result()
				msg = '{} result: {!r}'
				print(msg.format(future, res))
				results.append(res)

		return len(results)
