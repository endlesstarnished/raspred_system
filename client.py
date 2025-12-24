import grpc
import survey_pb2
import survey_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = survey_pb2_grpc.SurveyServiceStub(channel)
    
    # Создаем поток ответов
    def generate_answers():
        answers = [
            survey_pb2.Answer(question="Ваш возраст?", answer="25"),
            survey_pb2.Answer(question="Любимый язык?", answer="Python"),
            survey_pb2.Answer(question="Нравится ли gRPC?", answer="Да"),
        ]
        
        for answer in answers:
            yield answer
    
    # Отправляем на сервер
    response = stub.SubmitAnswers(generate_answers())
    print(f"Результат: {response.result}")
    print(f"Получено ответов: {response.count}")

if __name__ == '__main__':
    run()
