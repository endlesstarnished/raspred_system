import grpc
from concurrent import futures
import survey_pb2
import survey_pb2_grpc

class SurveyService(survey_pb2_grpc.SurveyServiceServicer):
    def SubmitAnswers(self, answers, context):
        count = 0
        print("Сервер: начал получать ответы...")
        
        for answer in answers:
            count += 1
            print(f"Сервер: получен ответ {count}:")
            print(f"  Вопрос ID: {answer.question_id}")
            print(f"  Пользователь ID: {answer.user_id}")
            print(f"  Ответ: {answer.answer_text}")
            print("-" * 30)
        
        print(f"Сервер: всего получено {count} ответов")
        
        return survey_pb2.Response(
            status="SUCCESS",
            answers_received=count,
            message=f"Спасибо! Ваши {count} ответов сохранены."
        )

def serve():
    print("Запуск gRPC сервера...")
    print("Порт: 50051")
    print("Ожидание подключений...")
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    survey_pb2_grpc.add_SurveyServiceServicer_to_server(SurveyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
