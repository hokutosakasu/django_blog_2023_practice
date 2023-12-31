# Generated by Django 3.2.11 on 2023-06-28 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20230626_1456'),
    ]

    sql = """
        CREATE OR REPLACE VIEW V_PostCategory AS
            SELECT
                post.id ,
                post.title,
                post.text,
                post.image,
                post.created_date,
                post.updated_data,
                post.category_id,
                category.category
            FROM
                blog_post post,
                blog_category category
            WHERE
                post.category_id=category.id
            ORDER BY
                post.created_date desc;
    """
    
    reverse_sql = """
        DROP VIEW IF EXISTS V_PostCategory;
    """

    operations = [
        migrations.RunSQL(sql, reverse_sql),
    ]
 
