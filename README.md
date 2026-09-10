# BizXtreme

BizXtreme is the extended BizX application/integration repository, including WebGL/Three.js, wallet, crypto, game, Aurora, and Chimera integration material.

## Language-separated implementations

- `nodejs/` — Node.js 20+ server/integration implementation.
- `java/` — Java 17+ implementation using Maven.
- `python/` — Python 3.10+ implementation.
- `javascript/` — browser JavaScript implementation where applicable.
- `typescript/` — TypeScript implementation where applicable.
- `web/` — browser/WebGL application material.
- `Assets/` — Unity/C# application assets and packaged resources.
- `docs/` — language-neutral architecture and integration documentation.

Source implementations are separated by programming language. Packaged APK/WebGL artifacts remain artifacts and are not represented as Java, Python, or Node.js source.

## Node.js

```bash
cd nodejs
npm test
npm start
```

## Java

```bash
cd java
mvn test
```

## Python

```bash
cd python
python -m unittest discover -s tests
```

Java and Python provide native application/service boundaries while Node.js provides the server/web integration foundation. Browser, TypeScript, Unity/C#, and packaged application material remain in their appropriate language/runtime trees.
