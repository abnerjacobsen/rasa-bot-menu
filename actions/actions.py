# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_handle_unidades",
                                    2: "action_handle_agendamento",
                                    3: "action_handle_agendamento_info",
                                    4: "action_handle_cancelamento",
                                    5: "action_handle_encerrar"},
                                "unidades_opcoes": {
                                    1: ("action_handle_unidades", "Mato Grosso"),
                                    2: ("action_handle_unidades", "Afonso Pena"),
                                    }
                                }
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Por favor, informe um número!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"Está opção não está disponível!")
            return [SlotSet('option', None)]

        # dispatcher.utter_message(text=f"Você escolheu a opção {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

class ActionHandleUnidades(Action):

    def name(self) -> Text:
        return "action_handle_unidades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """Sobre qual unidade você quer informações ?
            1. Unidade Mato Grosso
            2. Unidade Afonso Pena"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "unidades_opcoes")]
        else:
            # We are in a submenu
            message = "Aqui estão as informações sobre a unidade {}:\nHorário de atendimento: 08:00-17:00hs\nEspecialidades: Cardiologia\n\nDigite o número de uma opção de atendimento:\n1. Informações sobre unidades 🔥\n2. Agendamento 🌊\n3. Informações de agendamento ☕️\n4. Cancelamento 🧠\n"
            dispatcher.utter_message(text=message.format(suboption))

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]

class ActionHandleAgendamento(Action):

    def name(self) -> Text:
        return "action_handle_agendamento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Está opção ainda não foi implementada.

Digite o número de uma opção de atendimento:
  1. Informações sobre unidades 🔥
  2. Agendamento 🌊
  3. Informações de agendamento ☕️
  4. Cancelamento 🧠
  5. Encerrar atendimento"""

        dispatcher.utter_message(text=message)

        return []

class ActionHandleAgendamentoInfo(Action):

    def name(self) -> Text:
        return "action_handle_agendamento_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Está opção ainda não foi implementada.

Digite o número de uma opção de atendimento:
  1. Informações sobre unidades 🔥
  2. Agendamento 🌊
  3. Informações de agendamento ☕️
  4. Cancelamento 🧠
  5. Encerrar atendimento"""

        dispatcher.utter_message(text=message)

        return []

class ActionHandleCancelamento(Action):

    def name(self) -> Text:
        return "action_handle_cancelamento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Está opção ainda não foi implementada.

Digite o número de uma opção de atendimento:
  1. Informações sobre unidades 🔥
  2. Agendamento 🌊
  3. Informações de agendamento ☕️
  4. Cancelamento 🧠
  5. Encerrar atendimento"""

        dispatcher.utter_message(text=message)

        return []

class ActionHandleEncerrar(Action):

    def name(self) -> Text:
        return "action_handle_encerrar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Está opção ainda não foi implementada.

Digite o número de uma opção de atendimento:
  1. Informações sobre unidades 🔥
  2. Agendamento 🌊
  3. Informações de agendamento ☕️
  4. Cancelamento 🧠
  5. Encerrar atendimento"""

        dispatcher.utter_message(text=message)

        return []

