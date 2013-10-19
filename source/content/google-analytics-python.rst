Querying Google Analytics in Python
===================================

:date: 2013-10-19
:tags: python


I was implementing admin panel for a site and wanted to show the visitors count from Google Analytics but was soon frustrated to find that there was no simple way. Found out `this`_ post describing the process but it missed out many parts that I had to figure out myself. So, I'm writing this in hope that somebody will find it useful.

First of all you need to get a service account which will let you have a private key with which you can make the queries.

- Visit `Google Cloud Console`_ and create a new project if you don't already have one.
- Then select the project and go to ``APIs & auth`` > ``Registered apps`` on the left.
- Click on ``Register App``, choose whatever name you wish and ``Web Application`` as platform.
- On the next page, open ``Certificate`` panel, click on ``Generate Certificate``, download the presented private key and note the password.
- Under the ``Certificate`` panel, an email address should have appeared. Note it.

You need to give read access to the above email address in your analytics account.

- In Google Analytics, open the site's reporting section and click on ``Admin`` link on top-right.
- Under ``User Management``, add ``Read & Analyze`` permissions for the email address you noted previously.

You also need profile id of your Google Analytics account. Click on home icon and you should see a string like ``a9437494161w8843423p4789324``. The number part after ``p`` in it is your profile id (``4789324`` here). I couldn't find any more quicker and cleaner way to find it. Note it as well.

In Python, you need ``oauth2client`` and ``google-api-python-client`` packages installed. Here is a sample python script with which you can query a few metrics.

.. code-block:: python

    from apiclient.discovery import build
    from oauth2client.client import SignedJwtAssertionCredentials
    import httplib2

    def get_analytics_visitors():
        f = file('privatekey.p12', 'r') # EDIT THIS
        key = f.read()
        f.close()
        credentials = SignedJwtAssertionCredentials('replace_this@developer.gserviceaccount.com', # EDIT THIS
                                                    key,
                                                    scope='https://www.googleapis.com/auth/analytics.readonly')
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build('analytics', 'v3', http=http)
        data_query = service.data().ga().get(**{
            'ids': 'ga:YOUR_PROFILE_ID', # EDIT THIS
            'metrics': 'ga:visits,ga:visitors,ga:newVisits,ga:pageviews,ga:uniquePageviews,ga:visitBounceRate',
            'start_date': 'yesterday',
            'end_date': 'yesterday'
            })
        return data_query.execute()['totalsForAllResults']

    if __name__ == "__main__":
        print get_analytics_visitors()


Place the downloaded private key in same directory or set the proper path to it. Set your service account email address and Google Analytics profile id in the script. The script should work.

If you get ``NotImplementedError: PKCS12 format is not supported by the PyCrpto library. Try converting to a "PEM" (openssl pkcs12 -in xxxxx.p12 -nodes -nocerts > privatekey.pem) or using PyOpenSSL if native code is an option.``, then run ``openssl pkcs12 -in private.p12 -nodes -nocerts > privatekey.pem`` in terminal (account for the filenames). Enter the password that was presented when you downloaded the private key. It was most probably 'notasecret'.

Don't forget to change the private key filename in script to ``privatekey.pem``. If you still get the same error, just remove the header from the PEM file (edit in any text editor), so it begins with ``-----BEGIN PRIVATE KEY-----`` (solution found on `stackoverflow`_).

The script should finally work now without any problems.

Visit https://developers.google.com/analytics/devguides/reporting/core/dimsmets to see all the metrics and dimensions that you can use in your queries and https://developers.google.com/analytics/devguides/reporting/core/v3/reference for core reporting API reference.


.. _this: http://www.julianbez.com/blog/2013/05/31/query-google-analytics-api-with-a-service-account-in-python/
.. _Google Cloud Console: https://cloud.google.com/console
.. _stackoverflow: http://stackoverflow.com/questions/17993604/signedjwtassertioncredentials-on-appengine-doesnt-recognize-pem-key
