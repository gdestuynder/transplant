DEBUG = True

REPOSITORIES = [
    {
        "name": "transplant-src",
        "path": "ssh://hg@bitbucket.org/laggyluke/transplant-src"
    },
    {
        "name": "transplant-dst",
        "path": "ssh://hg@bitbucket.org/laggyluke/transplant-dst",
        "base": "ssh://hg@bitbucket.org/laggyluke/transplant-src"
    }
]

WORKDIR = '/tmp/transplant'
