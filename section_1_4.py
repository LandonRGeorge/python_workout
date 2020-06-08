def get_run():

    run_times = []

    while True:
        run_time = input('Enter 10km run time: :')

        if run_time == 'q':
            break

        else:
            run_times.append(float(run_time))

    num_runs = len(run_times)
    sum_times = sum(run_times)
    avg_time = sum_times / num_runs

    print(f'\nAverage of {avg_time}, over {num_runs} runs.')
