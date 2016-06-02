<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <artifactId>o11nplugin-{{name}}</artifactId>
    <packaging>dar</packaging>

    <parent>
        <artifactId>{{name}}-vro</artifactId>
        <groupId>{{package_prefix}}</groupId>
        <version>{{plugin_version}}</version>
    </parent>

    <dependencies>
        <!-- Default dependencies -->
        <dependency>
            <groupId>{{package_prefix}}</groupId>
            <artifactId>o11nplugin-{{name}}-core</artifactId>
        </dependency>
        <dependency>
            <groupId>{{package_prefix}}</groupId>
            <artifactId>o11nplugin-{{name}}-package</artifactId>
            <type>package</type>
        </dependency>

        <!-- Other dependencies -->
        <dependency>
            <groupId>com.vmware.o11n</groupId>
            <artifactId>o11n-spring-tools</artifactId>
            <version>${vco.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- dar file generation -->
            <plugin>
                <groupId>com.vmware.o11n.mojo.dar</groupId>
                <artifactId>maven-o11n-dar-plugin</artifactId>
                <version>${vco.version}</version>
                <extensions>true</extensions>
                <configuration>
                    <filtering>true</filtering>
                    <nonFilteredFileExtensions>
                        <string>package</string>
                    </nonFilteredFileExtensions>
                    <modules>
                        <jarModule>
                            <groupId>{{package_prefix}}</groupId>
                            <artifactId>o11nplugin-{{name}}-core</artifactId>
                        </jarModule>
                        <packageModule>
                            <groupId>{{package_prefix}}</groupId>
                            <artifactId>o11nplugin-{{name}}-package</artifactId>
                        </packageModule>
                    </modules>
                </configuration>
            </plugin>
            <!-- vso.xml generation -->
            <plugin>
                <groupId>com.vmware.o11n</groupId>
                <artifactId>o11n-vso-generator</artifactId>
                <version>${vco.version}</version>
                <executions>
                    <execution>
                        <id>Generate vso</id>
                        <goals>
                            <goal>vso</goal>
                        </goals>
                        <configuration>
                            <moduleBuilder>{{package_name}}.ModuleBuilder</moduleBuilder>
                        </configuration>
                    </execution>
                </executions>
                <dependencies>
                    <dependency>
                        <groupId>{{package_prefix}}</groupId>
                        <artifactId>o11nplugin-{{name}}-core</artifactId>
                        <version>${project.version}</version>
                        <scope>runtime</scope>
                    </dependency>
                </dependencies>
            </plugin>

            <!-- vmoapp file generation -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-antrun-plugin</artifactId>
                <executions>
                    <execution>
                        <id>CreateVmoApp</id>
                        <phase>package</phase>
                        <goals>
                            <goal>run</goal>
                        </goals>
                        <configuration>
                            <tasks>
                                <copy
                                    tofile="${basedir}/target/${project.artifactId}.${project.packaging}"
                                    flatten="true" overwrite="true" verbose="true" failonerror="true"
                                    file="${basedir}/target/${project.build.finalName}.${project.packaging}" />
                                <mkdir dir="${basedir}/target/VSO-INF" />
                                <copy todir="${basedir}/target/VSO-INF" overwrite="true" verbose="true" failonerror="true">
                                    <fileset dir="${basedir}/src/main/vmoapp/VSO-INF" />
                                </copy>
                                <jar destfile="${basedir}/target/${project.build.finalName}.vmoapp">
                                    <fileset dir="${basedir}/target/">
                                        <include name="${project.artifactId}.${project.packaging}" />
                                        <include name="VSO-INF/*" />
                                    </fileset>
                                </jar>
                            </tasks>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>build-helper-maven-plugin</artifactId>
                <version>1.5</version>
                <executions>
                    <execution>
                        <id>attach-artifacts</id>
                        <phase>package</phase>
                        <goals>
                            <goal>attach-artifact</goal>
                        </goals>
                        <configuration>
                            <artifacts>
                                <artifact>
                                    <file>${basedir}/target/${project.build.finalName}.vmoapp</file>
                                    <type>vmoapp</type>
                                </artifact>
                            </artifacts>
                        </configuration>
                    </execution>
                    <execution>
                        <id>ExtractVSOPluginVersion</id>
                        <phase>validate</phase>
                        <goals>
                            <goal>parse-version</goal>
                        </goals>
                        <configuration>
                            <propertyPrefix>vsoPluginVersion</propertyPrefix>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
