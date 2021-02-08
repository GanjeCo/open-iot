

from . import Topic

class Thing():

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.topics = []

        for arg in args:
            if isinstance(arg, Topic.Topic):
                self.topics.append(arg)

    def remove_topic(self, topic_to_remove):
        for topic in self.topics:
            if topic.topic == topic_to_remove:
                topic.do_unsubscribe()
                del topic
                break

    def add_topic(self, topics_to_add: Topic):
        for topic_to_add in topics_to_add:
            if isinstance(topic_to_add, Topic.Topic):
                self.topics.append(topic_to_add)
            else:
                raise Exception("topic to add must be a Topic instance")
