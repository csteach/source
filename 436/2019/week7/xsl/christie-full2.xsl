<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Collection</h2>
  <xsl:apply-templates/>
  </body>
  </html>
</xsl:template>

<xsl:template match="book">
  <p>
  <xsl:apply-templates select="title"/>
  <xsl:apply-templates select="author"/>
  <xsl:apply-templates select="price"/>
  </p>
</xsl:template>

<xsl:template match="title">
  <xsl:choose>
        <xsl:when test="../price &lt; 10">
          <span style="color:#ff00ff">
          <xsl:value-of select="."/>
          </span>
        </xsl:when>
        <xsl:otherwise>
          <span>Price too high: <xsl:value-of select="."/></span>
        </xsl:otherwise>
      </xsl:choose>
  <br />
</xsl:template>

<xsl:template match="author">
  Author: <span class="author"><xsl:value-of select="."/></span>
  <br />
</xsl:template>

<xsl:template match="price">
  Price: <span class="price"><xsl:value-of select="."/></span>
  <br />
</xsl:template>

</xsl:stylesheet>