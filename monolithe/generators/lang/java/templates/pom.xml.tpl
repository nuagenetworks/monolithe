<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>
   <groupId>{{ package_prefix }}</groupId>
   <artifactId>{{ name }}</artifactId>
   <version>{{library_version}}</version>
   <packaging>jar</packaging>

   <name>${project.groupId}:${project.artifactId}</name>
   <description>Java SDK for Nuage VSP Platform</description>
   <url>http://github.com/nuagenetworks/vspk-java</url>

   <licenses>
      <license>
         <name>Alcatel-Lucent Inc. License</name>
         <url>http://github.com/nuagenetworks/vspk-java/blob/{{ version }}/LICENSE</url>
         <distribution>repo</distribution>
      </license>
   </licenses>

   <developers>
      <developer>
         <name>Nuage Networks</name>
         <email>nuage-oss-support@alcatel-lucent.com</email>
         <organization>Nuage Networks</organization>
         <organizationUrl>http://www.nuagenetworks.net</organizationUrl>
      </developer>
   </developers>

   <scm>
      <connection>scm:git:git@github.com:nuagenetworks/vspk-java.git</connection>
      <developerConnection>scm:git:git@github.com:nuagenetworks/vspk-java.git</developerConnection>
      <url>git@github.com:nuagenetworks/vspk-java.git</url>
   </scm>

   <build>
      <plugins>
         <plugin>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.1</version>
            <configuration>
               <source>1.7</source>
               <target>1.7</target>
            </configuration>
         </plugin>
      </plugins>
   </build>

   <dependencies>
      <dependency>
         <groupId>net.nuagenetworks</groupId>
         <artifactId>bambou</artifactId>
         <version>2.0.21</version>
      </dependency>
   </dependencies>
</project>
