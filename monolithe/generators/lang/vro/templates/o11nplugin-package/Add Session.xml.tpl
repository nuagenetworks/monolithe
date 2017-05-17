<?xml version="1.0" encoding="UTF-8"?>
<workflow xmlns="http://vmware.com/vco/workflow" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://vmware.com/vco/workflow http://vmware.com/vco/workflow/Workflow-v4.xsd" root-name="item1" object-name="workflow:name=generic" id="41a66da3-1b10-4dff-883d-229f162eedea" version="4.0.8" api-version="6.0.0" allowed-operations="vef" restartMode="1" resumeFromFailedMode="0">
  <display-name><![CDATA[Add Session]]></display-name>
  <position y="50.0" x="100.0"></position>
  <input>
    <param name="apiUrl" type="string"></param>
    <param name="username" type="string"></param>
    <param name="password" type="SecureString"></param>
    <param name="enterprise" type="string"></param>
    <param name="certificate" type="string"></param>
    <param name="privateKey" type="string"></param>
    <param name="notificationsEnabled" type="boolean"></param>
    <param name="useJmsForNotifications" type="boolean"></param>
  </input>
  <output>
    <param name="session" type="VSPK:Session"></param>
  </output>
  <workflow-item name="item0" type="end" end-mode="0">
    <position y="45.40909090909091" x="384.5"></position>
  </workflow-item>
  <workflow-item name="item1" out-name="item0" type="task">
    <display-name><![CDATA[Scriptable task]]></display-name>
    <script encoded="false"><![CDATA[if (certificate && privateKey) {
   session = new VSPKSession(username, enterprise, apiUrl, certificate, privateKey);
} else if (password) {
   session = new VSPKSession(username, password, enterprise, apiUrl);
} else {
   throw "Must specify password or certificate/privateKey";
}

session.notificationsEnabled = notificationsEnabled;
session.useJmsForNotifications = useJmsForNotifications;
session.start();

VSPKSessionManager.addSession(session);]]></script>
    <in-binding>
      <bind name="apiUrl" type="string" export-name="apiUrl"></bind>
      <bind name="username" type="string" export-name="username"></bind>
      <bind name="password" type="SecureString" export-name="password"></bind>
      <bind name="enterprise" type="string" export-name="enterprise"></bind>
      <bind name="notificationsEnabled" type="boolean" export-name="notificationsEnabled"></bind>
      <bind name="useJmsForNotifications" type="boolean" export-name="useJmsForNotifications"></bind>
      <bind name="certificate" type="string" export-name="certificate"></bind>
      <bind name="privateKey" type="string" export-name="privateKey"></bind>
    </in-binding>
    <out-binding>
      <bind name="session" type="VSPK:Session" export-name="session"></bind>
    </out-binding>
    <position y="55.40909090909091" x="204.5"></position>
  </workflow-item>
  <presentation>
    <p-group>
      <title><![CDATA[Authentication]]></title>
      <p-param name="apiUrl">
        <desc><![CDATA[apiUrl]]></desc>
        <p-qual kind="static" name="mandatory" type="boolean"><![CDATA[true]]></p-qual>
      </p-param>
      <p-param name="username">
        <desc><![CDATA[username]]></desc>
        <p-qual kind="static" name="mandatory" type="boolean"><![CDATA[true]]></p-qual>
      </p-param>
      <p-param name="password">
        <desc><![CDATA[password]]></desc>
      </p-param>
      <p-param name="enterprise">
        <desc><![CDATA[enterprise]]></desc>
        <p-qual kind="static" name="mandatory" type="boolean"><![CDATA[true]]></p-qual>
      </p-param>
      <p-param name="certificate">
        <desc><![CDATA[certificate]]></desc>
        <p-qual name="textInput" type="void"><![CDATA[__NULL__]]></p-qual>
      </p-param>
      <p-param name="privateKey">
        <desc><![CDATA[privateKey]]></desc>
        <p-qual name="textInput" type="void"><![CDATA[__NULL__]]></p-qual>
      </p-param>
    </p-group>
    <p-step>
      <title><![CDATA[Notifications]]></title>
      <p-param name="useJmsForNotifications">
        <desc><![CDATA[useJmsForNotifications]]></desc>
        <p-qual kind="static" name="defaultValue" type="boolean"><![CDATA[true]]></p-qual>
      </p-param>
      <p-param name="notificationsEnabled">
        <desc><![CDATA[notificationsEnabled]]></desc>
        <p-qual kind="static" name="defaultValue" type="boolean"><![CDATA[true]]></p-qual>
      </p-param>
    </p-step>
  </presentation>
</workflow>