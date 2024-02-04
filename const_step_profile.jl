def const_step_profile(step_size = 15e-9, resolution=1): 

    step_times = np.arange(0,period,resolution)
    step_position = paa(step_times)
    print("Done with high res trajectory")

    current_pos = 0.0
    step_time = 0.0
    has_stepped = False

    event_time = [step_time]
    event_position = [current_pos]

    for step_time, nominal_pos in zip(step_times, step_position):

        if nominal_pos-current_pos >= step_size:
            # make a step

            current_pos += step_size
            has_stepped = True

        elif nominal_pos-current_pos <= -step_size:

            current_pos -= step_size
            has_stepped = True
        
        else:
            
            has_stepped = False

        if has_stepped:

            #print(f"events {len(event_time)}")

            event_time.append(step_time)
            event_position.append(current_pos)
    
    return (event_time, event_position)