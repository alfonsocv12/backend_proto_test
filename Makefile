protoc-swift:
	protoc -I=. --swift_out=. src/**/**/*.proto
	zip -r swift.zip src -i \*.swift