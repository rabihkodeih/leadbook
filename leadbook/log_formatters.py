import logging
from scrapy import logformatter


class SilentDroppedItemLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):  # @UnusedVariable
        return {
            'level': logging.NOTSET,
            'msg': logformatter.DROPPEDMSG,
            'args': {
                'exception': exception,
                'item': item,
            }
        }


# end of file
