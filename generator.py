import PyModuleGenerator

readme = open("README.md", "r", encoding="utf-8").read()

config: PyModuleGenerator.PyModuleGeneratorConfig = PyModuleGenerator.PyModuleGeneratorConfig(
    pythonCommand="py",    # Python command to use (python or python3 or py)

    modulePath="D:/Projects/VintedPyInterface/src",
    buildFolder="D:/Projects/VintedPyInterface/build",
    moduleName="VintedPyInterface",
    moduleVersion="0.1.0",
    moduleDescription="Interface for Vinted front end",
    moduleLongDescription=readme, # You can read file from README.md
    moduleLongDescriptionType="text/markdown",

    githubURL="https://github.com/ProfesseurIssou/VintedPyInterface",
    moduleAuthor="Alix Hamidou",
    moduleAuthorEmail="alix.hamidou@gmail.com",
    moduleLicense="MIT",

    moduleDependencies=[
        "selenium==4.6.1",
        "fake_useragent==1.1.3"

    ],
    moduleTags=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ], # https://pypi.org/classifiers/
)


PyModuleGenerator.PyModuleGenerator(
    config=config,
    clearBuildFolder=True,      # Erase the build folder after the build
    publishToPypi=True          # Publish the module to pypi
)
