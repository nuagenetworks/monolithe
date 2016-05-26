<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>
   <groupId>{{ package_prefix }}</groupId>
   <artifactId>{{ name }}</artifactId>
   <version>{{ version }}</version>

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
         <version>2.0.0</version>
      </dependency>
   </dependencies>

   <distributionManagement>
      <repository>
         <id>ArtifactoryServer</id>
         <name>ArtifactoryServer-releases</name>
         <url>http://135.121.41.87:8081/artifactory/libs-release-local</url>
      </repository>
   </distributionManagement>

</project>
