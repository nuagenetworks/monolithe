<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>{{package_prefix}}</groupId>
    <artifactId>{{name}}-vro</artifactId>
    <packaging>pom</packaging>
    <version>{{plugin_version}}</version>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <vco.version>6.0.3</vco.version>
    </properties>

    <repositories>
        <repository>
            <id>added-by-archetype</id>
            <name>This repo was added by the archetype. There are better way to handle it</name>
            <url>${repoUrl}</url>
        </repository>
    </repositories>

    <pluginRepositories>
        <pluginRepository>
            <id>added-by-archetype</id>
            <name>This repo was added by the archetype. There are better way to handle it</name>
            <url>${repoUrl}</url>
        </pluginRepository>
    </pluginRepositories>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>{{package_prefix}}</groupId>
                <artifactId>o11nplugin-{{name}}-core</artifactId>
                <version>${project.version}</version>
            </dependency>

            <dependency>
                <groupId>{{package_prefix}}</groupId>
                <artifactId>o11nplugin-{{name}}-package</artifactId>
                <version>${project.version}</version>
                <type>package</type>
            </dependency>

            <dependency>
                <groupId>com.vmware.o11n</groupId>
                <artifactId>o11n-provided-deps</artifactId>
                <version>${vco.version}</version>
                <scope>provided</scope>
                <type>pom</type>
            </dependency>

            <dependency>
                <groupId>com.vmware.o11n</groupId>
                <artifactId>o11n-spring-tools</artifactId>
                <version>${vco.version}</version>
            </dependency>

            <dependency>
                <groupId>com.vmware.o11n</groupId>
                <artifactId>o11n-sdkapi</artifactId>
                <version>${vco.version}</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <finalName>${artifactId}-${version}.${build.number}</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>1.3.1</version>
                <executions>
                    <execution>
                        <id>enforce-versions</id>
                        <goals>
                             <goal>enforce</goal>
                        </goals>
                        <configuration>
                            <rules>
                                <requireMavenVersion>
                                    <version>3.0.1</version>
                                </requireMavenVersion>
                                <requireJavaVersion>
                                    <version>1.6</version>
                                </requireJavaVersion>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <configuration>
                        <source>1.7</source>
                        <target>1.7</target>
                        <compilerArgs>
                            <arg>-J-Xss4m</arg>
                        </compilerArgs>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
    <modules>
        <module>o11nplugin-{{name}}-core</module>
        <module>o11nplugin-{{name}}-package</module>
        <module>o11nplugin-{{name}}</module>
    </modules>
</project>