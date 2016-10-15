<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <artifactId>o11nplugin-{{name}}-package</artifactId>
    <packaging>package</packaging>

    <parent>
        <artifactId>{{name}}-vro</artifactId>
        <groupId>{{package_prefix}}</groupId>
        <version>{{plugin_version}}</version>
    </parent>

    <properties>
        <!-- vCO packages are signed. Create your own JKS keystore that contains 
            a key-pair under the alias _DunesRSA_Alias_ -->
        <!-- This keystore is meant for easier initial setup and should not be 
            used in production -->
        <keystoreLocation>archetype.keystore</keystoreLocation>
        <keystorePassword>password123</keystorePassword>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>com.vmware.o11n.mojo.pkg</groupId>
                <artifactId>maven-o11n-package-plugin</artifactId>
                <version>${vco.version}</version>
                <extensions>true</extensions>
                <configuration>
                    <packageName>{{package_prefix}}</packageName>
                    <!-- Set the local path to the *.vmokeystore file used to sign the content -->
                    <keystoreLocation>${keystoreLocation}</keystoreLocation>
                    <keystorePassword>${keystorePassword}</keystorePassword>
                    <includes>
                        <include>**/*.element_info.xml</include>
                    </includes>
                    <packageFileName>o11nplugin-{{name}}-package-${project.version}</packageFileName>
                    <!-- For release build change to vf. It will lock the workflows -->
                    <allowedMask>vef</allowedMask>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
