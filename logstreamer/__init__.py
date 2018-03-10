import logging

from inotify_simple import INotify, flags


ONE_SHOT = 'one-shot'
FROM_START = 'from-start'
TAIL = 'tail'


class Logstreamer():
    def __init__(self, path, target, splitter='\n', mode=ONE_SHOT):
        """
        Create new Logstreamer.

        Logstreamer setups inotify watches on file set specified by `path` and send lines to target
        and monitors creation of new files

        :param path: a glob pattern specifying file names to watch
        :param target: callable or Queue-like object with method `put`
        :param splitter: delimiter char, callable or regexp matching the log line (default: `\n`)
        """
        self.path = path
        self.target = target
        self.splitter = self.make_splitter(splitter)
        self.mode = mode

    def make_splitter(self, splitter):
        if isinstance(splitter, str):
            return lambda x: x.split(splitter)
        else:
            raise Exception("splitter based on %t is not implemented yet" % splitter)

    def run(self):
        """
        Run logstreamer
        """

    def watch_new(self):
        """
        Watch for new files in directory
        """


    def handle_by_extention(self):
        """
        Read compressed files like .gz
        Return file like object
        """

    def watch_file(self, filename):
        """
        Watch current file line by line
        """
        with INotify() as inotify:
            logging.info("starting watch on %s (inode %d)", filename, inode)
            inotify.add_watch(filename, flags.MODIFY | flags.CLOSE_WRITE)
            for i in yield_until_eof(f):
                yield i
            for i in self._watch_until_closed(f, inotify):
                yield i
            logging.info("finished watch on %s (inode %d)", filename, inode)
