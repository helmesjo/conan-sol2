from conans import ConanFile, CMake, tools
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class LuaConan(ConanFile):
    name = "sol2"
    version = "3.2.0"
    description = "sol is a C++ library binding to Lua."
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "lua", "scripting", "embedded")
    url = "https://github.com/helmesjo/conan-sol"
    homepage = "https://github.com/ThePhD/sol2"
    author = "helmesjo <helmesjo@live.com>"
    license = "MIT"
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    requires = ("lua/5.3.5")

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/ThePhd/sol2"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="33abe8f6937c9d7eb2e4c6d80dadde4feb4b9cc88ba8fd1cebf7e2776aebe897")
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()