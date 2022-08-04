

def mapping_pinch_isolated_streams(user_data):

    streams_to_analyse = [stream['id'] for stream in user_data["streams"]]  # all are being considered

    data = {
        "platform":
            {
                "streams": user_data["streams"],
                "pinch_delta_T_min": user_data["pinch_delta_T_min"],
                "fuels_data": user_data["fuels_data"],
                "streams_to_analyse": streams_to_analyse,
                "interest_rate": user_data["interest_rate"]
            }
    }

    return data
