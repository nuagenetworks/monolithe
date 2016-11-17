<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workflow xmlns="http://vmware.com/vco/workflow" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://vmware.com/vco/workflow http://vmware.com/vco/workflow/Workflow-v4.xsd" root-name="item1" object-name="workflow:name=generic" id="6e47e60d-fba0-406d-a4d2-d727a42146c4"  version="{{ workflow_version }}" api-version="6.0.0" allowed-operations="vef" restartMode="1" resumeFromFailedMode="0" >
<display-name><![CDATA[Remove Session]]></display-name>
<ref-types><![CDATA[(VSPK:Session)]]></ref-types>
<position x='100.0' y='50.0'/>
<input><param name='session' type='VSPK:Session' >
</param>
</input><workflow-item name='item0' type='end' end-mode='0' >
<position x='384.5' y='45.40909090909091'/>
</workflow-item>
<workflow-item name='item1' out-name='item0' type='task' >
<display-name><![CDATA[Scriptable task]]></display-name>
<script encoded='false'><![CDATA[session.stop();

VSPKSessionManager.removeSession(session);]]></script>
<in-binding><bind name='session' type='VSPK:Session' export-name="session" ></bind>
</in-binding><out-binding></out-binding><position x='204.5' y='55.40909090909091'/>
</workflow-item>
<presentation>
<p-param name="session"><desc><![CDATA[session]]></desc>
<p-qual name="contextualParameter" type="void" ><![CDATA[__NULL__]]></p-qual></p-param>
</presentation></workflow>