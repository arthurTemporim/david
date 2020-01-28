from david.brain import Brain
from david.constants import CONTEXT_ATTRIBUTE, ENTITIES_ATTRIBUTE, INTENTS_ATTRIBUTE
from david.dialog import Dialog


class Assistant:
    def __init__(self):
        self.brain = Brain()
        self.dialog = Dialog()
        self.train()

    def train(self):
        self.brain.train()
        self.dialog.train()

    def respond(self, input, context={}):
        message = self.brain.process(input)

        intents = message.get(INTENTS_ATTRIBUTE)
        entities = message.get(ENTITIES_ATTRIBUTE)
        context = message.get(CONTEXT_ATTRIBUTE)

        # print("intents", intents)
        dialog_node = self.dialog.dialog(input, context, intents, entities)
        return {
            "context": context,
            "intents": intents,
            "entities": entities,
            "output": dialog_node["output"],
        }
