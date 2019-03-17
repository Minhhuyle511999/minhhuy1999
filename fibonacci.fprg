<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2019-03-17 08:08:47 PM"/>
        <attribute name="created" value="QWRtaW47QURNSU4tUEM7MjAxOS0wMy0xMTswOToxMDozMyBQTTsyMzE5"/>
        <attribute name="edited" value="QWRtaW47QURNSU4tUEM7MjAxOS0wMy0xNzswODowODo0NyBQTTszOzI0NDY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="size" type="Integer" array="False" size=""/>
            <input variable="size"/>
            <declare name="counter" type="Integer" array="False" size=""/>
            <assign variable="counter" expression="0"/>
            <declare name="fib" type="Integer" array="True" size="size"/>
            <for variable="counter" start="0" end="size-1" direction="inc" step="1">
                <if expression="counter=0 or counter=1">
                    <then>
                        <assign variable="fib[counter]" expression="counter"/>
                    </then>
                    <else>
                        <assign variable="fib[counter]" expression="fib[counter-2]+fib[counter-1]"/>
                    </else>
                </if>
                <output expression="fib[counter]" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>
