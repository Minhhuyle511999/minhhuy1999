<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2019-03-11 09:06:30 PM"/>
        <attribute name="created" value="QWRtaW47QURNSU4tUEM7MjAxOS0wMy0xMTswODo1MDo1OSBQTTsyMzMw"/>
        <attribute name="edited" value="QWRtaW47QURNSU4tUEM7MjAxOS0wMy0xMTswOTowNjozMCBQTTsxOzI0Mjk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a" type="Real" array="False" size=""/>
            <declare name="b" type="Real" array="False" size=""/>
            <declare name="c" type="Real" array="False" size=""/>
            <declare name="dt" type="Integer" array="False" size=""/>
            <declare name="x" type="Real" array="False" size=""/>
            <declare name="x1" type="Real" array="False" size=""/>
            <declare name="x2" type="Real" array="False" size=""/>
            <output expression="&quot;enter a&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;enter b&quot;" newline="True"/>
            <input variable="b"/>
            <output expression="&quot;enter c&quot;" newline="True"/>
            <input variable="c"/>
            <if expression="a=0">
                <then>
                    <if expression="b=0">
                        <then>
                            <if expression="c=0">
                                <then>
                                    <output expression="&quot;The equation has a multitude of solutions&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;The equation have no solution &quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <if expression="c=0">
                                <then>
                                    <output expression="&quot;x=0&quot;" newline="True"/>
                                </then>
                                <else>
                                    <assign variable="x" expression="-c/b"/>
                                    <output expression="&quot;x=&quot;&amp; x" newline="True"/>
                                </else>
                            </if>
                        </else>
                    </if>
                </then>
                <else>
                    <assign variable="dt" expression="b*b-4*a*c"/>
                    <if expression="dt &lt; 0">
                        <then>
                            <output expression="&quot;The equation has a multitude of solutions&quot;" newline="True"/>
                        </then>
                        <else>
                            <if expression="dt = 0">
                                <then>
                                    <assign variable="x" expression="-b/(2*a)"/>
                                    <output expression="&quot;x=&quot; &amp; x" newline="True"/>
                                </then>
                                <else>
                                    <assign variable="x1" expression="(-b + sqrt(dt))/(2*a)"/>
                                    <assign variable="x2" expression="(-b - sqrt(dt))/(2*a)"/>
                                    <output expression="&quot;x1=&quot; &amp; x1" newline="True"/>
                                    <output expression="&quot;x2=&quot; &amp; x2" newline="True"/>
                                </else>
                            </if>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
