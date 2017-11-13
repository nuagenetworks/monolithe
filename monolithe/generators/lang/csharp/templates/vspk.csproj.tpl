<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />
  <PropertyGroup>
    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
    <Platform Condition=" '$(Platform)' == '' ">AnyCPU</Platform>
    <ProjectGuid>a12da736-a2ca-47e2-9a20-991330b39f45</ProjectGuid>
    <OutputType>Library</OutputType>
    <AppDesignerFolder>Properties</AppDesignerFolder>
    <RootNamespace>vspk</RootNamespace>
    <AssemblyName>net.nuagenetworks.vspk</AssemblyName>
    <TargetFrameworkVersion>v4.5.2</TargetFrameworkVersion>
    <FileAlignment>512</FileAlignment>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\Debug\</OutputPath>
    <DefineConstants>DEBUG;TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">
    <DebugType>pdbonly</DebugType>
    <Optimize>true</Optimize>
    <OutputPath>bin\Release\</OutputPath>
    <DefineConstants>TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <ItemGroup>
    <Reference Include="net.nuagenetworks.bambou, Version=1.0.6521.25133, Culture=neutral, processorArchitecture=MSIL">
      <HintPath>$(SolutionDir)\packages\net.nuagenetworks.bambou.dll.1.1.1\lib\net452\net.nuagenetworks.bambou.dll</HintPath>
    </Reference>
    <Reference Include="Newtonsoft.Json, Version=10.0.0.0, Culture=neutral, PublicKeyToken=30ad4fe6b2a6aeed, processorArchitecture=MSIL">
      <HintPath>$(SolutionDir)\packages\Newtonsoft.Json.10.0.3\lib\net45\Newtonsoft.Json.dll</HintPath>
    </Reference>
    <Reference Include="System"/>
    <Reference Include="System.Core"/>
    <Reference Include="System.Xml.Linq"/>
    <Reference Include="System.Data.DataSetExtensions"/>
    <Reference Include="Microsoft.CSharp"/>
    <Reference Include="System.Data"/>
    <Reference Include="System.Net.Http"/>
    <Reference Include="System.Xml"/>
  </ItemGroup>
  <ItemGroup>
    {%- for rest_name,specification in specifications.items() %}
    <Compile Include="{{ specification.entity_name| replace(" ", "_")}}.cs" />
    <Compile Include="{{ specification.entity_name_plural| replace(" ", "_")}}Fetcher.cs" />
    {%- endfor %}
    <Compile Include="SdkInfo.cs" />
    <Compile Include="VSDSession.cs" />
    <Compile Include="Properties\AssemblyInfo.cs" />
  </ItemGroup>
  <ItemGroup>
    <None Include="packages.config" />
  </ItemGroup>
  <Import Project="$(MSBuildToolsPath)\Microsoft.CSharp.targets" />
 </Project>

