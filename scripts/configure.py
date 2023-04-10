# This script generates and updates project configuration files.

# Run this script with rvscaffold in PYTHONPATH
import rvscaffold as scaffold

class Project(scaffold.Java):
    def script_path_text(self): return __file__
    def repository_name(self): return 'hookless-noexception'
    def pretty_name(self): return 'Hookless adapter for NoException'
    def pom_description(self): return 'Hookless reactive adapter for NoException library.'
    def inception_year(self): return 2015
    def jdk_version(self): return 17
    def stagean_annotations(self): return True
    def complete_javadoc(self): return False
    def has_website(self): return False
    
    def dependencies(self):
        yield from super().dependencies()
        yield self.use_noexception()
        yield self.use_noexception_slf4j()
        yield self.use_fastutil()
        yield self.use_guava()
        yield self.use('io.micrometer:micrometer-core:1.6.4')
        yield self.use('io.opentracing:opentracing-util:0.33.0')
        yield self.use_junit()
        yield self.use_hamcrest()
        yield self.use('org.awaitility:awaitility:4.0.3', 'test')
        yield self.use('org.junit-pioneer:junit-pioneer:0.9.0')
        yield self.use_slf4j_test()
    
    def javadoc_links(self):
        yield from super().javadoc_links()
        yield 'https://noexception.machinezoo.com/javadocs/core/'

Project().generate()
