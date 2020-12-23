from cnn_model.predict import make_prediction


def test_make_prediction():
    result = make_prediction(
        img_url="https://hotdogdetectorbucket.s3.amazonaws.com/test_data/hotdog-b48b740d9d292d8f3243529d834cd89af866ab47.jpg",
        img_id="test")

    assert result["version"] == "0.1.0"
    assert result["prediction"] == "hotdog"
    assert (result["score"] > 0.5) and (result["score"] < 1.0)
    
