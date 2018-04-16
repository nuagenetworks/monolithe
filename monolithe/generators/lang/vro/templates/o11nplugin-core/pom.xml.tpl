<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <artifactId>o11nplugin-{{name}}-core</artifactId>
    <packaging>jar</packaging>

    <parent>
        <artifactId>{{name}}-vro</artifactId>
        <groupId>{{package_prefix}}</groupId>
        <version>{{plugin_version}}</version>
    </parent>

    <dependencies>
        <dependency>
            <groupId>com.vmware.o11n</groupId>
            <artifactId>o11n-provided-deps</artifactId>
            <scope>provided</scope>
            <type>pom</type>
        </dependency>

        <dependency>
            <groupId>com.vmware.o11n</groupId>
            <artifactId>o11n-sdkapi</artifactId>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>net.nuagenetworks</groupId>
            <artifactId>vro-plugin-base</artifactId>
            <version>1.0.7</version>
        </dependency>
    </dependencies>
</project>
