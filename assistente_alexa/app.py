from flask import Flask
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, is_request_type
from flask_ask_sdk.skill_adapter import SkillAdapter
import acoes

app = Flask(__name__)
sb = SkillBuilder()


class LaunchHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        print("LAUNCH HANDLER CHAMADO!")
        fala = "Assistente ativado. O que você quer fazer?"
        return (
            handler_input.response_builder
            .speak(fala)
            .ask(fala)
            .response
        )


class ComandoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ComandoIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        comando = slots["comando"].value
        print(f"SLOT RECEBIDO: '{comando}'")
        resposta = acoes.executar(comando)
        return (
            handler_input.response_builder
            .speak(resposta)
            .ask("O que mais você quer fazer?")
            .response
        )


class FechарHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            is_intent_name("AMAZON.StopIntent")(handler_input) or
            is_intent_name("AMAZON.CancelIntent")(handler_input)
        )

    def handle(self, handler_input):
        print("FECHAR HANDLER CHAMADO!")
        fala = "Assistente encerrado. Até mais!"
        return (
            handler_input.response_builder
            .speak(fala)
            .set_should_end_session(True)
            .response
        )


sb.add_request_handler(LaunchHandler())
sb.add_request_handler(ComandoHandler())
sb.add_request_handler(FechарHandler())

skill_adapter = SkillAdapter(
    skill=sb.create(),
    skill_id="amzn1.ask.skill.development",
    app=app
)

@app.route("/", methods=["POST"])
def invoke_skill():
    print("REQUISIÇÃO RECEBIDA!")
    return skill_adapter.dispatch_request()


if __name__ == "__main__":
    app.run(port=5000, debug=False)