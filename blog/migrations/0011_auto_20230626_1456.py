# Generated by Django 3.2.11 on 2023-06-26 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_image'),
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

    perations = [
        migrations.RunSQL(sql, reverse_sql),
    ]