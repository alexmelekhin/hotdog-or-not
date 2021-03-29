# Hotdog Or Not Classifier

Курсовая работа по дисциплине ПОСИИ

Ссылка на используемый датасет: <https://hotdogdetectorbucket.s3.amazonaws.com/train_dataset/dataset.zip>

## Описание

В данном проекте выполнено:
* В [ноутбуке](https://github.com/metra4ok/hotdog-or-not/blob/master/notebooks/Hotdog_or_not_classifier.ipynb) разработана простая CNN нейросеть на tensorflow, осуществляющая классификацию изображений на два класса: хотдог и не хотдог.
* Модель оформлена в виде [пакета](https://github.com/metra4ok/hotdog-or-not/tree/master/packages/cnn_model), написаны тесты с использованием библиотек pytest и tox.
* Разработано [Web-API](https://github.com/metra4ok/hotdog-or-not/tree/master/packages/web_api) с использованием библиотеки Flask, тесты написаны с библиотеками pytest и tox.
* Разработанный микросервис запускается в docker-контейнере, все необходимые инструкции размещены в [Dockerfile](https://github.com/metra4ok/hotdog-or-not/blob/master/Dockerfile).
