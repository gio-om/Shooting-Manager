from data import shooting_types_name


async def guess_type_of_shooting(state_data):
    answer = ''
    if state_data['simple_shooting'] >= 2:
        answer += shooting_types_name['simple_shooting']
    elif state_data['advanced_shooting'] >= 2:
        answer += shooting_types_name['advanced_shooting']
    elif state_data['video_shooting'] >= 2:
        answer += shooting_types_name['video_shooting']
    else:
        answer += shooting_types_name['individual_shooting']

    return answer
